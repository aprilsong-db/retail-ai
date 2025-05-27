-- Employee Tasks table for retail store management
-- Supports the store companion app with task tracking, priorities, and assignments
CREATE TABLE IF NOT EXISTS employee_tasks (
    task_id STRING NOT NULL,
    employee_id STRING NOT NULL,
    store_id STRING NOT NULL,
    task_title STRING NOT NULL,
    task_description STRING,
    task_type STRING NOT NULL, -- 'BOPIS', 'Service', 'Restock', 'Cleaning', 'Training', 'Administrative', 'Customer_Service', 'Inventory'
    task_category STRING NOT NULL, -- 'Operations', 'Customer_Service', 'Inventory_Management', 'Maintenance', 'Administrative'
    priority_level STRING NOT NULL, -- 'Low', 'Medium', 'High', 'Critical', 'Urgent'
    task_status STRING NOT NULL, -- 'Pending', 'In_Progress', 'Completed', 'Cancelled', 'On_Hold', 'Overdue'
    
    -- Scheduling information
    assigned_date DATE NOT NULL,
    due_date DATE,
    due_time TIME,
    estimated_duration_minutes INT, -- Estimated time to complete in minutes
    actual_duration_minutes INT, -- Actual time taken to complete
    
    -- Assignment details
    assigned_by STRING, -- Employee ID of who assigned the task
    assigned_to STRING NOT NULL, -- Employee ID of who should complete the task
    department STRING, -- Department where task should be performed
    location_details STRING, -- Specific location within store (e.g., "Floor 2", "Electronics Section")
    
    -- Customer/Order related information (for BOPIS, Service tasks)
    customer_id STRING,
    customer_name STRING,
    order_id STRING,
    order_number STRING,
    
    -- Product/Inventory related information (for Restock, Inventory tasks)
    product_sku STRING,
    product_name STRING,
    quantity_required INT,
    
    -- Task completion tracking
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    notes STRING, -- Notes added during task execution
    completion_notes STRING, -- Notes added upon completion
    
    -- Recurring task information
    is_recurring BOOLEAN DEFAULT FALSE,
    recurrence_pattern STRING, -- 'Daily', 'Weekly', 'Monthly', 'Custom'
    parent_task_id STRING, -- Reference to parent task if this is a recurring instance
    
    -- Performance and quality metrics
    quality_score DECIMAL(3,2), -- Quality rating (1.00 to 5.00)
    customer_satisfaction_score DECIMAL(3,2), -- Customer satisfaction if applicable
    requires_manager_approval BOOLEAN DEFAULT FALSE,
    approved_by STRING, -- Manager who approved completion
    approved_at TIMESTAMP,
    
    -- System tracking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    created_by STRING,
    updated_by STRING,
    
    -- Additional metadata
    tags ARRAY<STRING>, -- Tags for categorization and filtering
    attachments ARRAY<STRING>, -- File paths or URLs to related documents/images
    dependencies ARRAY<STRING>, -- Task IDs that must be completed before this task
    
    -- Mobile app specific fields
    requires_photo_proof BOOLEAN DEFAULT FALSE,
    photo_urls ARRAY<STRING>, -- URLs to photos taken during task completion
    gps_location STRING, -- GPS coordinates where task was completed
    device_id STRING, -- Device used to complete the task
    
    CONSTRAINT pk_employee_tasks PRIMARY KEY (task_id)
) 
USING DELTA
TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = 'true',
    'delta.autoOptimize.autoCompact' = 'true'
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_employee_tasks_employee_date 
ON employee_tasks (assigned_to, assigned_date);

CREATE INDEX IF NOT EXISTS idx_employee_tasks_store_date 
ON employee_tasks (store_id, assigned_date);

CREATE INDEX IF NOT EXISTS idx_employee_tasks_status_priority 
ON employee_tasks (task_status, priority_level);

CREATE INDEX IF NOT EXISTS idx_employee_tasks_type_category 
ON employee_tasks (task_type, task_category);

CREATE INDEX IF NOT EXISTS idx_employee_tasks_due_date 
ON employee_tasks (due_date, due_time);

CREATE INDEX IF NOT EXISTS idx_employee_tasks_customer 
ON employee_tasks (customer_id) WHERE customer_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_employee_tasks_order 
ON employee_tasks (order_id) WHERE order_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_employee_tasks_product 
ON employee_tasks (product_sku) WHERE product_sku IS NOT NULL;

-- Create views for common queries used by the store companion app

-- View for today's tasks by employee
CREATE OR REPLACE VIEW employee_daily_tasks AS
SELECT 
    task_id,
    employee_id,
    store_id,
    task_title,
    task_description,
    task_type,
    task_category,
    priority_level,
    task_status,
    due_time,
    estimated_duration_minutes,
    customer_name,
    order_number,
    product_name,
    location_details,
    department,
    notes,
    CASE 
        WHEN due_time IS NOT NULL AND due_time < CURRENT_TIME() AND task_status IN ('Pending', 'In_Progress') 
        THEN TRUE 
        ELSE FALSE 
    END AS is_overdue,
    CASE 
        WHEN priority_level IN ('Critical', 'Urgent') THEN 1
        WHEN priority_level = 'High' THEN 2
        WHEN priority_level = 'Medium' THEN 3
        ELSE 4
    END AS priority_sort_order
FROM employee_tasks
WHERE assigned_date = CURRENT_DATE()
ORDER BY priority_sort_order, due_time;

-- View for task performance metrics
CREATE OR REPLACE VIEW task_performance_metrics AS
SELECT 
    assigned_to AS employee_id,
    store_id,
    assigned_date,
    COUNT(*) AS total_tasks,
    COUNT(CASE WHEN task_status = 'Completed' THEN 1 END) AS completed_tasks,
    COUNT(CASE WHEN task_status = 'Pending' THEN 1 END) AS pending_tasks,
    COUNT(CASE WHEN task_status = 'In_Progress' THEN 1 END) AS in_progress_tasks,
    COUNT(CASE WHEN task_status = 'Overdue' THEN 1 END) AS overdue_tasks,
    AVG(CASE WHEN quality_score IS NOT NULL THEN quality_score END) AS avg_quality_score,
    AVG(CASE WHEN customer_satisfaction_score IS NOT NULL THEN customer_satisfaction_score END) AS avg_customer_satisfaction,
    AVG(CASE WHEN actual_duration_minutes IS NOT NULL THEN actual_duration_minutes END) AS avg_completion_time_minutes,
    ROUND(
        COUNT(CASE WHEN task_status = 'Completed' THEN 1 END) * 100.0 / COUNT(*), 
        2
    ) AS completion_percentage
FROM employee_tasks
GROUP BY assigned_to, store_id, assigned_date;

-- View for manager task oversight
CREATE OR REPLACE VIEW manager_task_overview AS
SELECT 
    store_id,
    assigned_date,
    department,
    task_type,
    priority_level,
    COUNT(*) AS task_count,
    COUNT(CASE WHEN task_status = 'Completed' THEN 1 END) AS completed_count,
    COUNT(CASE WHEN task_status IN ('Pending', 'In_Progress') AND due_time < CURRENT_TIME() THEN 1 END) AS overdue_count,
    COUNT(CASE WHEN priority_level IN ('Critical', 'Urgent') THEN 1 END) AS high_priority_count,
    AVG(CASE WHEN actual_duration_minutes IS NOT NULL THEN actual_duration_minutes END) AS avg_duration_minutes
FROM employee_tasks
WHERE assigned_date >= CURRENT_DATE() - INTERVAL 7 DAYS
GROUP BY store_id, assigned_date, department, task_type, priority_level
ORDER BY assigned_date DESC, overdue_count DESC, high_priority_count DESC; 