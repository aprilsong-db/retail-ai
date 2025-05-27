USE IDENTIFIER(:database);

-- Insert store data for retail chain
INSERT INTO stores (
    store_id, store_name, store_address, store_city, store_state, store_zipcode, 
    store_country, store_phone, store_email, store_manager_id, opening_date, 
    store_area_sqft, is_open_24_hours, latitude, longitude, region_id
) VALUES
-- New York Area Stores
('001', 'Downtown', '123 Main St', 'New York', 'NY', '10001', 'USA', '(212) 555-1234', 'downtown@com', 'mgr_001', '2015-05-20', 5000.0, true, 40.7128, -74.006, '1'),
('002', 'Uptown', '456 Broadway', 'New York', 'NY', '10002', 'USA', '(212) 555-5678', 'uptown@com', 'mgr_002', '2018-07-15', 3000.0, false, 40.7138, -74.007, '1'),
('003', 'Manhattan Mini', '789 5th Avenue', 'New York', 'NY', '10003', 'USA', '(212) 555-9012', 'manhattanmini@com', 'mgr_003', '2016-03-10', 2500.0, true, 40.7589, -73.9851, '1'),
('004', 'Bronx', '321 Fordham Road', 'New York', 'NY', '10458', 'USA', '(718) 555-3456', 'bronx@com', 'mgr_004', '2017-08-22', 4500.0, false, 40.8614, -73.8827, '1'),
('005', 'Queens Corner', '567 Queens Blvd', 'New York', 'NY', '11375', 'USA', '(718) 555-7890', 'queens@com', 'mgr_005', '2019-01-15', 3800.0, true, 40.7282, -73.8618, '1'),
('006', 'Brooklyn Heights', '123 Montague St', 'New York', 'NY', '11201', 'USA', '(718) 555-4321', 'brooklyn@com', 'mgr_006', '2020-03-01', 2800.0, false, 40.6935, -73.9916, '1'),
('007', 'Staten Island', '789 Hylan Blvd', 'New York', 'NY', '10305', 'USA', '(718) 555-8765', 'statenisland@com', 'mgr_007', '2018-06-15', 4200.0, true, 40.6065, -74.0752, '1'),
('008', 'Harlem', '456 Malcolm X Blvd', 'New York', 'NY', '10027', 'USA', '(212) 555-9876', 'harlem@com', 'mgr_008', '2017-11-30', 3500.0, false, 40.8116, -73.9465, '1'),
('009', 'Lower East Side', '234 Delancey St', 'New York', 'NY', '10002', 'USA', '(212) 555-3456', 'les@com', 'mgr_009', '2019-08-22', 2600.0, true, 40.7168, -73.9861, '1'),

-- Boston Area Stores
('010', 'Back Bay', '100 Boylston St', 'Boston', 'MA', '02116', 'USA', '(617) 555-1234', 'backbay@com', 'mgr_010', '2018-03-15', 3200.0, false, 42.3518, -71.0711, '1'),
('011', 'Beacon Hill', '89 Charles St', 'Boston', 'MA', '02114', 'USA', '(617) 555-2345', 'beaconhill@com', 'mgr_011', '2019-05-01', 2800.0, false, 42.356, -71.0705, '1'),
('012', 'South End', '540 Tremont St', 'Boston', 'MA', '02118', 'USA', '(617) 555-3456', 'southend@com', 'mgr_012', '2017-09-12', 3500.0, true, 42.3433, -71.0726, '1'),
('013', 'Fenway', '123 Brookline Ave', 'Boston', 'MA', '02215', 'USA', '(617) 555-4567', 'fenway@com', 'mgr_013', '2020-01-15', 4000.0, false, 42.3467, -71.0972, '1'),
('014', 'Cambridge', '750 Memorial Dr', 'Boston', 'MA', '02139', 'USA', '(617) 555-5678', 'cambridge@com', 'mgr_014', '2018-11-30', 3800.0, true, 42.3576, -71.1009, '1'),

-- Philadelphia Area Stores
('015', 'Center City', '1200 Market St', 'Philadelphia', 'PA', '19107', 'USA', '(215) 555-1234', 'centercity@com', 'mgr_015', '2019-04-01', 4500.0, true, 39.9526, -75.1652, '1'),
('016', 'South Philly', '1001 S 9th St', 'Philadelphia', 'PA', '19147', 'USA', '(215) 555-2345', 'southphilly@com', 'mgr_016', '2017-07-15', 3300.0, false, 39.9375, -75.1571, '1'),
('017', 'University City', '3401 Walnut St', 'Philadelphia', 'PA', '19104', 'USA', '(215) 555-3456', 'univcity@com', 'mgr_017', '2020-02-28', 2900.0, true, 39.9522, -75.1932, '1'),
('018', 'Northern Liberties', '180 W Girard Ave', 'Philadelphia', 'PA', '19123', 'USA', '(215) 555-4567', 'noliberties@com', 'mgr_018', '2018-09-01', 3700.0, false, 39.9697, -75.1398, '1'),
('019', 'Rittenhouse Square', '1800 Walnut St', 'Philadelphia', 'PA', '19103', 'USA', '(215) 555-5678', 'rittenhouse@com', 'mgr_019', '2019-11-15', 4100.0, true, 39.9496, -75.1709, '1'),

-- Washington DC Area Stores
('020', 'Georgetown', '1200 Wisconsin Ave NW', 'Washington D.C.', 'DC', '20007', 'USA', '(202) 555-1234', 'georgetown@com', 'mgr_020', '2018-04-15', 3800.0, false, 38.9055, -77.067, '2'),
('021', 'Dupont Circle', '1800 P St NW', 'Washington D.C.', 'DC', '20036', 'USA', '(202) 555-2345', 'dupont@com', 'mgr_021', '2019-06-01', 3200.0, true, 38.9097, -77.0409, '2'),
('022', 'Capitol Hill', '400 East Capitol St NE', 'Washington D.C.', 'DC', '20003', 'USA', '(202) 555-3456', 'capitolhill@com', 'mgr_022', '2017-08-30', 2900.0, false, 38.8898, -77.0001, '2'),
('023', 'Adams Morgan', '1700 Columbia Rd NW', 'Washington D.C.', 'DC', '20009', 'USA', '(202) 555-4567', 'adamsmorgan@com', 'mgr_023', '2020-03-15', 3500.0, true, 38.9222, -77.0421, '2'),
('024', 'U Street', '1400 U St NW', 'Washington D.C.', 'DC', '20009', 'USA', '(202) 555-5678', 'ustreet@com', 'mgr_024', '2019-09-01', 3100.0, false, 38.9169, -77.0312, '2'),

-- Baltimore Area Stores
('025', 'Inner Harbor', '600 E Pratt St', 'Baltimore', 'MD', '21202', 'USA', '(410) 555-1234', 'innerharbor@com', 'mgr_025', '2018-07-01', 4200.0, true, 39.2866, -76.6089, '2'),
('026', 'Fells Point', '1700 Thames St', 'Baltimore', 'MD', '21231', 'USA', '(410) 555-2345', 'fellspoint@com', 'mgr_026', '2019-04-15', 3300.0, false, 39.2819, -76.5943, '2'),
('027', 'Canton', '2800 O''Donnell St', 'Baltimore', 'MD', '21224', 'USA', '(410) 555-3456', 'canton@com', 'mgr_027', '2017-11-30', 3600.0, true, 39.2792, -76.5762, '2'),
('028', 'Federal Hill', '1000 Light St', 'Baltimore', 'MD', '21230', 'USA', '(410) 555-4567', 'fedhill@com', 'mgr_028', '2020-01-15', 2800.0, false, 39.2775, -76.6134, '2'),
('029', 'Mount Vernon', '600 N Charles St', 'Baltimore', 'MD', '21201', 'USA', '(410) 555-5678', 'mtvernon@com', 'mgr_029', '2019-08-01', 3400.0, true, 39.2967, -76.6156, '2'),

-- Richmond Area Stores
('030', 'Carytown', '3500 W Cary St', 'Richmond', 'VA', '23221', 'USA', '(804) 555-1234', 'carytown@com', 'mgr_030', '2018-05-15', 3700.0, false, 37.5552, -77.4856, '2'),
('031', 'Shockoe Bottom', '1800 E Main St', 'Richmond', 'VA', '23223', 'USA', '(804) 555-2345', 'shockoe@com', 'mgr_031', '2019-03-01', 3200.0, true, 37.5315, -77.4267, '2'),
('032', 'Fan District', '2200 W Main St', 'Richmond', 'VA', '23220', 'USA', '(804) 555-3456', 'fandistrict@com', 'mgr_032', '2017-10-15', 2900.0, false, 37.5539, -77.4673, '2'),
('033', 'Scott''s Addition', '3000 W Broad St', 'Richmond', 'VA', '23230', 'USA', '(804) 555-4567', 'scottsadd@com', 'mgr_033', '2020-02-01', 3800.0, true, 37.5668, -77.4747, '2'),
('034', 'Church Hill', '2500 E Broad St', 'Richmond', 'VA', '23223', 'USA', '(804) 555-5678', 'churchhill@com', 'mgr_034', '2019-07-15', 3100.0, false, 37.5338, -77.4178, '2'),

-- Atlanta Area Stores
('036', 'Buckhead', '3255 Peachtree Rd', 'Atlanta', 'GA', '30305', 'USA', '(404) 555-1234', 'buckhead@com', 'mgr_036', '2017-05-15', 4200.0, false, 33.8406, -84.3795, '3'),
('037', 'Midtown Atlanta', '950 W Peachtree St', 'Atlanta', 'GA', '30309', 'USA', '(404) 555-2345', 'midtown@com', 'mgr_037', '2019-03-01', 3500.0, true, 33.7815, -84.3885, '3'),
('046', 'Midtown West', '950 West Peachtree St NW', 'Atlanta', 'GA', '30309', 'USA', '(404) 555-1234', 'midtownatl@com', 'mgr_046', '2018-04-15', 3400.0, true, 33.7815, -84.3857, '3'),
('047', 'Buckhead North', '3035 Peachtree Rd NE', 'Atlanta', 'GA', '30305', 'USA', '(404) 555-2345', 'buckheadnorth@com', 'mgr_047', '2017-12-10', 3800.0, false, 33.8399, -84.3801, '3'),
('048', 'Virginia Highland', '1001 Virginia Ave NE', 'Atlanta', 'GA', '30306', 'USA', '(404) 555-3456', 'vahighland@com', 'mgr_048', '2019-02-20', 2700.0, false, 33.7817, -84.3571, '3'),
('049', 'Little Five Points', '421 Moreland Ave NE', 'Atlanta', 'GA', '30307', 'USA', '(404) 555-4567', 'l5p@com', 'mgr_049', '2018-09-05', 2500.0, true, 33.7618, -84.349, '3'),
('050', 'West Midtown', '1100 Howell Mill Rd NW', 'Atlanta', 'GA', '30318', 'USA', '(404) 555-5678', 'westmidtown@com', 'mgr_050', '2020-01-15', 3300.0, false, 33.7861, -84.4113, '3'),

-- Miami Area Stores
('038', 'South Beach', '1020 Ocean Dr', 'Miami', 'FL', '33139', 'USA', '(305) 555-1234', 'southbeach@com', 'mgr_038', '2018-12-01', 2900.0, true, 25.7825, -80.1324, '3'),
('039', 'Brickell', '901 S Miami Ave', 'Miami', 'FL', '33130', 'USA', '(305) 555-2345', 'brickell@com', 'mgr_039', '2017-09-15', 3800.0, false, 25.7657, -80.1937, '3'),
('041', 'Little Havana', '1200 SW 8th St', 'Miami', 'FL', '33135', 'USA', '(305) 555-3456', 'littlehavana@com', 'mgr_041', '2019-03-15', 3200.0, true, 25.7655, -80.2179, '3'),
('042', 'Wynwood', '250 NW 24th St', 'Miami', 'FL', '33127', 'USA', '(305) 555-4567', 'wynwood@com', 'mgr_042', '2020-01-10', 2900.0, false, 25.7994, -80.1989, '3'),
('043', 'Coral Gables', '2200 Ponce de Leon Blvd', 'Miami', 'FL', '33134', 'USA', '(305) 555-5678', 'coralgables@com', 'mgr_043', '2017-11-20', 3500.0, false, 25.7501, -80.259, '3'),
('044', 'Coconut Grove', '3330 Grand Ave', 'Miami', 'FL', '33133', 'USA', '(305) 555-6789', 'coconutgrove@com', 'mgr_044', '2018-08-05', 2600.0, true, 25.7269, -80.2425, '3'),
('045', 'Downtown Miami', '100 SE 2nd St', 'Miami', 'FL', '33131', 'USA', '(305) 555-7890', 'downtown@com', 'mgr_045', '2019-06-01', 3100.0, true, 25.7743, -80.1937, '3'),

-- Charlotte Area Stores
('040', 'Dilworth', '1235 East Blvd', 'Charlotte', 'NC', '28203', 'USA', '(704) 555-1234', 'dilworth@com', 'mgr_040', '2019-04-01', 3300.0, false, 35.2089, -80.8486, '3'),
('051', 'South End', '2100 South Blvd', 'Charlotte', 'NC', '28203', 'USA', '(704) 555-1234', 'southend@com', 'mgr_051', '2019-03-15', 3500.0, true, 35.2098, -80.8577, '3'),
('052', 'NoDa', '3201 N Davidson St', 'Charlotte', 'NC', '28205', 'USA', '(704) 555-2345', 'noda@com', 'mgr_052', '2018-07-01', 2800.0, false, 35.2424, -80.8024, '3'),
('053', 'Plaza Midwood', '1600 Central Ave', 'Charlotte', 'NC', '28205', 'USA', '(704) 555-3456', 'plazamidwood@com', 'mgr_053', '2017-11-15', 3200.0, true, 35.2206, -80.8099, '3'),
('054', 'Uptown', '300 S Tryon St', 'Charlotte', 'NC', '28202', 'USA', '(704) 555-4567', 'uptown@com', 'mgr_054', '2020-02-01', 2900.0, true, 35.2271, -80.8431, '3'),
('055', 'Myers Park', '1024 Providence Rd', 'Charlotte', 'NC', '28207', 'USA', '(704) 555-5678', 'myerspark@com', 'mgr_055', '2019-08-15', 3800.0, false, 35.2033, -80.8241, '3'),

-- Chicago Area Stores
('056', 'Loop', '200 N Michigan Ave', 'Chicago', 'IL', '60601', 'USA', '(312) 555-1234', 'loop@com', 'mgr_056', '2018-05-01', 4200.0, true, 41.8857, -87.6244, '4'),
('057', 'Wicker Park', '1600 N Milwaukee Ave', 'Chicago', 'IL', '60647', 'USA', '(312) 555-2345', 'wickerpark@com', 'mgr_057', '2019-06-15', 3500.0, false, 41.9103, -87.6731, '4'),
('058', 'Lincoln Park', '2400 N Clark St', 'Chicago', 'IL', '60614', 'USA', '(312) 555-3456', 'lincolnpark@com', 'mgr_058', '2017-09-01', 3800.0, true, 41.9256, -87.6412, '4'),
('059', 'Logan Square', '2800 N Milwaukee Ave', 'Chicago', 'IL', '60618', 'USA', '(312) 555-4567', 'logan@com', 'mgr_059', '2020-03-01', 3100.0, false, 41.9302, -87.7024, '4'),
('060', 'River North', '500 N State St', 'Chicago', 'IL', '60654', 'USA', '(312) 555-5678', 'rivernorth@com', 'mgr_060', '2019-04-15', 4000.0, true, 41.8907, -87.6278, '4'),

-- Detroit Area Stores
('061', 'Midtown Detroit', '4400 Woodward Ave', 'Detroit', 'MI', '48201', 'USA', '(313) 555-1234', 'midtown@com', 'mgr_061', '2018-08-01', 3600.0, true, 42.3516, -83.0602, '4'),
('062', 'Corktown', '1700 Michigan Ave', 'Detroit', 'MI', '48216', 'USA', '(313) 555-2345', 'corktown@com', 'mgr_062', '2019-05-15', 3200.0, false, 42.3316, -83.0768, '4'),
('063', 'Eastern Market', '2934 Russell St', 'Detroit', 'MI', '48207', 'USA', '(313) 555-3456', 'easternmarket@com', 'mgr_063', '2017-12-01', 4100.0, true, 42.3476, -83.0419, '4'),
('064', 'New Center', '3011 W Grand Blvd', 'Detroit', 'MI', '48202', 'USA', '(313) 555-4567', 'newcenter@com', 'mgr_064', '2020-02-15', 3400.0, false, 42.3702, -83.0751, '4'),
('065', 'Rivertown', '1600 E Jefferson Ave', 'Detroit', 'MI', '48207', 'USA', '(313) 555-5678', 'rivertown@com', 'mgr_065', '2019-07-01', 3700.0, true, 42.3366, -83.0297, '4'),

-- Indianapolis Area Stores
('066', 'Mass Ave', '400 Massachusetts Ave', 'Indianapolis', 'IN', '46204', 'USA', '(317) 555-1234', 'massave@com', 'mgr_066', '2018-06-15', 3300.0, true, 39.7703, -86.1519, '4'),
('067', 'Broad Ripple', '6280 N College Ave', 'Indianapolis', 'IN', '46220', 'USA', '(317) 555-2345', 'broadripple@com', 'mgr_067', '2019-09-01', 2900.0, false, 39.8703, -86.1445, '4'),
('068', 'Fountain Square', '1043 Virginia Ave', 'Indianapolis', 'IN', '46203', 'USA', '(317) 555-3456', 'fountainsq@com', 'mgr_068', '2017-10-15', 3100.0, true, 39.7536, -86.142, '4'),
('069', 'Downtown Indy', '50 S Meridian St', 'Indianapolis', 'IN', '46204', 'USA', '(317) 555-4567', 'downtownindy@com', 'mgr_069', '2020-01-01', 3600.0, true, 39.7668, -86.1577, '4'),

-- Kansas City Area Stores
('134', 'Plaza', '4750 Broadway', 'Kansas City', 'MO', '64112', 'USA', '(816) 555-1234', 'plaza@com', 'mgr_134', '2018-05-15', 4100.0, true, 39.042, -94.5906, '4'),
('135', 'Westport', '4050 Pennsylvania Ave', 'Kansas City', 'MO', '64111', 'USA', '(816) 555-2345', 'westport@com', 'mgr_135', '2019-09-01', 3200.0, false, 39.0505, -94.5906, '4'),
('136', 'Crossroads', '2020 Baltimore Ave', 'Kansas City', 'MO', '64108', 'USA', '(816) 555-3456', 'crossroads@com', 'mgr_136', '2017-10-15', 2900.0, true, 39.0914, -94.5836, '4'),
('137', 'River Market', '411 Delaware St', 'Kansas City', 'MO', '64105', 'USA', '(816) 555-4567', 'rivermarket@com', 'mgr_137', '2020-04-01', 3600.0, false, 39.1089, -94.5829, '4'),

-- Phoenix Area Stores
('070', 'Downtown Phoenix', '333 E Jefferson St', 'Phoenix', 'AZ', '85004', 'USA', '(602) 555-1234', 'dtphoenix@com', 'mgr_070', '2018-06-15', 4200.0, true, 33.4484, -112.074, '5'),
('071', 'Scottsdale', '7014 E Camelback Rd', 'Phoenix', 'AZ', '85251', 'USA', '(602) 555-2345', 'scottsdale@com', 'mgr_071', '2019-03-01', 3800.0, false, 33.4994, -111.9289, '5'),
('072', 'Tempe', '2000 E Rio Salado Pkwy', 'Phoenix', 'AZ', '85281', 'USA', '(602) 555-3456', 'tempe@com', 'mgr_072', '2017-08-15', 4500.0, true, 33.4316, -111.9083, '5'),
('073', 'Glendale', '7700 W Arrowhead Towne Center', 'Phoenix', 'AZ', '85308', 'USA', '(602) 555-4567', 'glendale@com', 'mgr_073', '2020-01-10', 3200.0, false, 33.6377, -112.215, '5'),
('074', 'Mesa', '1230 S Val Vista Dr', 'Phoenix', 'AZ', '85204', 'USA', '(602) 555-5678', 'mesa@com', 'mgr_074', '2019-05-20', 3600.0, true, 33.3903, -111.7516, '5'),

-- Las Vegas Area Stores
('075', 'Strip', '3500 Las Vegas Blvd S', 'Las Vegas', 'NV', '89109', 'USA', '(702) 555-1234', 'strip@com', 'mgr_075', '2018-12-01', 5000.0, true, 36.1147, -115.1728, '6'),
('076', 'Downtown Vegas', '301 Fremont St', 'Las Vegas', 'NV', '89101', 'USA', '(702) 555-2345', 'downtownvegas@com', 'mgr_076', '2017-07-15', 3800.0, true, 36.1699, -115.1398, '6'),
('077', 'Summerlin', '1980 Festival Plaza Dr', 'Las Vegas', 'NV', '89135', 'USA', '(702) 555-3456', 'summerlin@com', 'mgr_077', '2019-09-01', 4200.0, false, 36.1575, -115.3368, '6'),
('078', 'Henderson', '2300 Paseo Verde Pkwy', 'Las Vegas', 'NV', '89052', 'USA', '(702) 555-4567', 'henderson@com', 'mgr_078', '2020-02-15', 3500.0, false, 36.0145, -115.0874, '6'),
('079', 'Spring Valley', '4178 S Fort Apache Rd', 'Las Vegas', 'NV', '89147', 'USA', '(702) 555-5678', 'springvalley@com', 'mgr_079', '2018-04-01', 3300.0, true, 36.1087, -115.2977, '6'),

-- San Francisco Area Stores (Enhanced with more locations)
('080', 'Financial District', '343 Sansome St', 'San Francisco', 'CA', '94104', 'USA', '(415) 555-1234', 'fidi@com', 'mgr_080', '2017-06-01', 3200.0, false, 37.7936, -122.4014, '6'),
('081', 'Mission District', '2558 Mission St', 'San Francisco', 'CA', '94110', 'USA', '(415) 555-2345', 'mission@com', 'mgr_081', '2019-08-15', 2800.0, true, 37.7562, -122.4186, '6'),
('082', 'Hayes Valley', '432 Octavia St', 'San Francisco', 'CA', '94102', 'USA', '(415) 555-3456', 'hayes@com', 'mgr_082', '2018-03-01', 2500.0, false, 37.7765, -122.4242, '6'),
('083', 'Marina', '2040 Chestnut St', 'San Francisco', 'CA', '94123', 'USA', '(415) 555-4567', 'marina@com', 'mgr_083', '2020-01-15', 3000.0, false, 37.8009, -122.4368, '6'),
('084', 'Sunset District', '1200 Irving St', 'San Francisco', 'CA', '94122', 'USA', '(415) 555-5678', 'sunset@com', 'mgr_084', '2017-11-01', 3400.0, true, 37.7642, -122.4682, '6'),
('153', 'Castro', '2300 Market St', 'San Francisco', 'CA', '94114', 'USA', '(415) 555-6789', 'castro@com', 'mgr_153', '2019-04-15', 2900.0, false, 37.7609, -122.4350, '6'),
('154', 'Chinatown', '800 Grant Ave', 'San Francisco', 'CA', '94108', 'USA', '(415) 555-7890', 'chinatown@com', 'mgr_154', '2018-09-01', 2200.0, true, 37.7946, -122.4058, '6'),
('155', 'North Beach', '1650 Stockton St', 'San Francisco', 'CA', '94133', 'USA', '(415) 555-8901', 'northbeach@com', 'mgr_155', '2017-12-15', 2600.0, false, 37.8024, -122.4089, '6'),
('156', 'Nob Hill', '1200 California St', 'San Francisco', 'CA', '94109', 'USA', '(415) 555-9012', 'nobhill@com', 'mgr_156', '2020-03-01', 2800.0, false, 37.7919, -122.4147, '6'),
('157', 'SOMA', '350 Townsend St', 'San Francisco', 'CA', '94107', 'USA', '(415) 555-0123', 'soma@com', 'mgr_157', '2019-07-15', 3500.0, true, 37.7749, -122.3959, '6'),
('158', 'Richmond District', '3800 Geary Blvd', 'San Francisco', 'CA', '94118', 'USA', '(415) 555-1357', 'richmond@com', 'mgr_158', '2018-05-20', 3100.0, false, 37.7816, -122.4635, '6'),
('159', 'Haight-Ashbury', '1700 Haight St', 'San Francisco', 'CA', '94117', 'USA', '(415) 555-2468', 'haight@com', 'mgr_159', '2019-11-01', 2700.0, true, 37.7693, -122.4489, '6'),
('160', 'Potrero Hill', '1200 18th St', 'San Francisco', 'CA', '94107', 'USA', '(415) 555-3579', 'potrero@com', 'mgr_160', '2020-06-15', 2900.0, false, 37.7615, -122.3972, '6'),
('161', 'Presidio Heights', '3200 Sacramento St', 'San Francisco', 'CA', '94115', 'USA', '(415) 555-4680', 'presidio@com', 'mgr_161', '2017-08-30', 3300.0, false, 37.7886, -122.4394, '6'),
('162', 'Fillmore', '1800 Fillmore St', 'San Francisco', 'CA', '94115', 'USA', '(415) 555-5791', 'fillmore@com', 'mgr_162', '2018-10-10', 2800.0, true, 37.7849, -122.4326, '6'),

-- Seattle Area Stores
('085', 'Capitol Hill Seattle', '1525 Broadway', 'Seattle', 'WA', '98122', 'USA', '(206) 555-1234', 'caphill@com', 'mgr_085', '2018-07-01', 3100.0, true, 47.6147, -122.3207, '7'),
('086', 'Ballard', '5701 24th Ave NW', 'Seattle', 'WA', '98107', 'USA', '(206) 555-2345', 'ballard@com', 'mgr_086', '2019-04-15', 3600.0, false, 47.6705, -122.3828, '7'),
('087', 'Queen Anne', '2121 Queen Anne Ave N', 'Seattle', 'WA', '98109', 'USA', '(206) 555-3456', 'queenanne@com', 'mgr_087', '2017-09-01', 2900.0, false, 47.6372, -122.3566, '7'),
('088', 'South Lake Union', '400 Fairview Ave N', 'Seattle', 'WA', '98109', 'USA', '(206) 555-4567', 'slu@com', 'mgr_088', '2020-03-01', 4000.0, true, 47.6221, -122.3331, '7'),
('089', 'West Seattle', '4555 California Ave SW', 'Seattle', 'WA', '98116', 'USA', '(206) 555-5678', 'westseattle@com', 'mgr_089', '2018-11-15', 3300.0, false, 47.5613, -122.3872, '7'),

-- Portland Area Stores
('090', 'Pearl District', '1231 NW Couch St', 'Portland', 'OR', '97209', 'USA', '(503) 555-1234', 'pearl@com', 'mgr_090', '2017-12-01', 3700.0, false, 45.5233, -122.6843, '7'),
('091', 'Hawthorne', '3590 SE Hawthorne Blvd', 'Portland', 'OR', '97214', 'USA', '(503) 555-2345', 'hawthorne@com', 'mgr_091', '2019-06-15', 2800.0, true, 45.512, -122.6274, '7'),
('092', 'Alberta Arts', '1504 NE Alberta St', 'Portland', 'OR', '97211', 'USA', '(503) 555-3456', 'alberta@com', 'mgr_092', '2018-08-01', 2600.0, false, 45.5589, -122.6499, '7'),
('093', 'Division Street', '3632 SE Division St', 'Portland', 'OR', '97202', 'USA', '(503) 555-4567', 'division@com', 'mgr_093', '2020-02-01', 3100.0, true, 45.505, -122.626, '7'),
('094', 'Northwest District', '2375 NW Thurman St', 'Portland', 'OR', '97210', 'USA', '(503) 555-5678', 'nwdistrict@com', 'mgr_094', '2019-10-15', 3400.0, false, 45.5352, -122.6991, '7'),

-- Boise Area Stores
('095', 'Downtown Boise', '821 W Idaho St', 'Boise', 'ID', '83702', 'USA', '(208) 555-1234', 'dtboise@com', 'mgr_095', '2018-05-01', 3200.0, true, 43.6167, -116.2023, '7'),
('100', 'North End', '1520 N 13th St', 'Boise', 'ID', '83702', 'USA', '(208) 555-6789', 'northend@com', 'mgr_100', '2019-06-15', 2800.0, false, 43.6289, -116.202, '7'),
('101', 'Boise Bench', '2520 Vista Ave', 'Boise', 'ID', '83705', 'USA', '(208) 555-7890', 'bench@com', 'mgr_101', '2017-09-01', 3100.0, true, 43.5923, -116.2157, '7'),
('102', 'Hyde Park', '1501 N 13th St', 'Boise', 'ID', '83702', 'USA', '(208) 555-8901', 'hydepark@com', 'mgr_102', '2020-03-15', 2600.0, false, 43.6287, -116.2019, '7'),
('103', 'East End', '815 Warm Springs Ave', 'Boise', 'ID', '83712', 'USA', '(208) 555-9012', 'eastend@com', 'mgr_103', '2018-07-01', 2900.0, true, 43.6127, -116.1891, '7'),

-- Salt Lake City Area Stores
('096', 'Sugar House', '2100 S 1100 E', 'Salt Lake City', 'UT', '84106', 'USA', '(801) 555-2345', 'sugarhouse@com', 'mgr_096', '2019-03-15', 3500.0, false, 40.7247, -111.8561, '8'),
('104', 'Downtown SLC', '400 S State St', 'Salt Lake City', 'UT', '84111', 'USA', '(801) 555-3456', 'dtslc@com', 'mgr_104', '2017-11-01', 4200.0, true, 40.7608, -111.891, '8'),
('105', 'The Avenues', '402 E 3rd Ave', 'Salt Lake City', 'UT', '84103', 'USA', '(801) 555-4567', 'avenues@com', 'mgr_105', '2019-08-15', 2800.0, false, 40.7747, -111.8789, '8'),
('106', '9th and 9th', '900 E 900 S', 'Salt Lake City', 'UT', '84105', 'USA', '(801) 555-5678', 'ninth@com', 'mgr_106', '2018-04-01', 3100.0, true, 40.7508, -111.8646, '8'),
('107', 'Capitol Hill SLC', '350 N State St', 'Salt Lake City', 'UT', '84103', 'USA', '(801) 555-6789', 'capitol@com', 'mgr_107', '2020-02-01', 2900.0, false, 40.7774, -111.8882, '8'),

-- Denver Area Stores
('097', 'LoDo', '1701 Wynkoop St', 'Denver', 'CO', '80202', 'USA', '(303) 555-3456', 'lodo@com', 'mgr_097', '2017-08-01', 4000.0, true, 39.7534, -104.9994, '8'),
('108', 'Highland', '2532 15th St', 'Denver', 'CO', '80211', 'USA', '(303) 555-7890', 'highland@com', 'mgr_108', '2019-05-15', 3200.0, false, 39.7575, -105.0109, '8'),
('109', 'Cherry Creek', '2800 E 2nd Ave', 'Denver', 'CO', '80206', 'USA', '(303) 555-8901', 'cherrycreek@com', 'mgr_109', '2018-06-01', 3800.0, true, 39.7179, -104.9567, '8'),
('110', 'Capitol Hill Denver', '1200 Grant St', 'Denver', 'CO', '80203', 'USA', '(303) 555-9012', 'caphilldenver@com', 'mgr_110', '2020-04-01', 2700.0, false, 39.7349, -104.9841, '8'),
('111', 'RiNo', '2601 Larimer St', 'Denver', 'CO', '80205', 'USA', '(303) 555-0123', 'rino@com', 'mgr_111', '2019-09-15', 3400.0, true, 39.7594, -104.9847, '8'),

-- Colorado Springs Area Stores
('098', 'Old Colorado City', '2501 W Colorado Ave', 'Colorado Springs', 'CO', '80904', 'USA', '(719) 555-4567', 'oldcolorado@com', 'mgr_098', '2020-01-15', 3300.0, false, 38.8461, -104.8594, '8'),
('112', 'Downtown Springs', '115 E Pikes Peak Ave', 'Colorado Springs', 'CO', '80903', 'USA', '(719) 555-1234', 'dtsprings@com', 'mgr_112', '2018-03-01', 3600.0, true, 38.8339, -104.8208, '8'),
('113', 'Broadmoor', '1 Lake Ave', 'Colorado Springs', 'CO', '80906', 'USA', '(719) 555-2345', 'broadmoor@com', 'mgr_113', '2019-07-15', 4100.0, false, 38.7897, -104.848, '8'),
('114', 'North Springs', '7915 N Academy Blvd', 'Colorado Springs', 'CO', '80920', 'USA', '(719) 555-3456', 'nsprings@com', 'mgr_114', '2017-12-01', 3200.0, true, 38.9327, -104.797, '8'),
('115', 'Powers Center', '5640 Powers Center Point', 'Colorado Springs', 'CO', '80920', 'USA', '(719) 555-4567', 'powers@com', 'mgr_115', '2019-11-15', 3500.0, false, 38.9018, -104.7474, '8'),

-- Omaha Area Stores
('099', 'Old Market', '1022 Howard St', 'Omaha', 'NE', '68102', 'USA', '(402) 555-5678', 'oldmarket@com', 'mgr_099', '2018-11-01', 3600.0, true, 41.2565, -95.9345, '9'),
('116', 'Dundee', '5001 Underwood Ave', 'Omaha', 'NE', '68132', 'USA', '(402) 555-6789', 'dundee@com', 'mgr_116', '2019-04-15', 2800.0, false, 41.2649, -95.9908, '9'),
('117', 'Benson', '6051 Maple St', 'Omaha', 'NE', '68104', 'USA', '(402) 555-7890', 'benson@com', 'mgr_117', '2017-07-01', 3200.0, true, 41.2841, -95.9977, '9'),
('118', 'Aksarben', '2200 S 67th St', 'Omaha', 'NE', '68106', 'USA', '(402) 555-8901', 'aksarben@com', 'mgr_118', '2020-05-01', 3400.0, false, 41.2419, -96.0197, '9'),

-- Wichita Area Stores
('129', 'Old Town Wichita', '300 N Mead St', 'Wichita', 'KS', '67202', 'USA', '(316) 555-1234', 'oldtown@com', 'mgr_129', '2019-04-01', 3100.0, false, 37.6897, -97.3375, '9'),
('130', 'College Hill', '3302 E Douglas Ave', 'Wichita', 'KS', '67208', 'USA', '(316) 555-2345', 'collegehill@com', 'mgr_130', '2018-08-15', 2800.0, true, 37.6868, -97.2951, '9'),
('131', 'Delano', '555 W Douglas Ave', 'Wichita', 'KS', '67213', 'USA', '(316) 555-3456', 'delano@com', 'mgr_131', '2017-12-01', 3300.0, false, 37.6868, -97.3475, '9'),
('132', 'East Central', '2721 E Central Ave', 'Wichita', 'KS', '67214', 'USA', '(316) 555-4567', 'eastcentral@com', 'mgr_132', '2020-01-15', 2900.0, true, 37.6868, -97.3097, '9'),
('133', 'Riverside', '924 W Central Ave', 'Wichita', 'KS', '67203', 'USA', '(316) 555-5678', 'riverside@com', 'mgr_133', '2019-07-01', 3500.0, false, 37.6868, -97.3597, '9'),

-- Hawaii Stores
('119', 'Waikiki Beach', '2255 Kalakaua Ave', 'Honolulu', 'HI', '96815', 'USA', '(808) 555-1234', 'waikiki@com', 'mgr_119', '2019-10-15', 3000.0, true, 21.2793, -157.8283, '10'),
('120', 'Ala Moana', '1450 Ala Moana Blvd', 'Honolulu', 'HI', '96814', 'USA', '(808) 555-2345', 'alamoana@com', 'mgr_120', '2018-06-01', 4200.0, false, 21.2906, -157.843, '10'),
('121', 'Kapahulu', '725 Kapahulu Ave', 'Honolulu', 'HI', '96816', 'USA', '(808) 555-3456', 'kapahulu@com', 'mgr_121', '2019-03-15', 2800.0, false, 21.2843, -157.815, '10'),
('122', 'Kaimuki', '3618 Waialae Ave', 'Honolulu', 'HI', '96816', 'USA', '(808) 555-4567', 'kaimuki@com', 'mgr_122', '2017-11-01', 3100.0, false, 21.2824, -157.7989, '10'),
('123', 'Manoa Valley', '2752 Woodlawn Dr', 'Honolulu', 'HI', '96822', 'USA', '(808) 555-5678', 'manoa@com', 'mgr_123', '2020-02-15', 2900.0, false, 21.3097, -157.8099, '10'),

-- Alaska Stores
('124', 'Downtown Anchorage', '320 W 5th Ave', 'Anchorage', 'AK', '99501', 'USA', '(907) 555-1234', 'downtownanchorage@com', 'mgr_124', '2018-07-01', 3800.0, true, 61.2176, -149.8951, '10'),
('125', 'Midtown Anchorage', '1200 W Northern Lights Blvd', 'Anchorage', 'AK', '99503', 'USA', '(907) 555-2345', 'midtownanchorage@com', 'mgr_125', '2019-05-15', 4200.0, true, 61.195, -149.9002, '10'),
('126', 'South Anchorage', '11409 Business Blvd', 'Anchorage', 'AK', '99515', 'USA', '(907) 555-3456', 'southanc@com', 'mgr_126', '2017-09-01', 3600.0, false, 61.1181, -149.878, '10'),
('127', 'Eagle River', '12001 Business Blvd', 'Anchorage', 'AK', '99577', 'USA', '(907) 555-4567', 'eagleriver@com', 'mgr_127', '2020-03-01', 3200.0, false, 61.3293, -149.568, '10'),
('128', 'Spenard', '1000 W Northern Lights Blvd', 'Anchorage', 'AK', '99503', 'USA', '(907) 555-5678', 'spenard@com', 'mgr_128', '2018-11-15', 3400.0, true, 61.195, -149.9002, '10'),

-- Los Angeles Area Stores
('138', 'Downtown LA', '350 S Grand Ave', 'Los Angeles', 'CA', '90071', 'USA', '(213) 555-1234', 'dtla@com', 'mgr_138', '2018-06-15', 4200.0, true, 34.0522, -118.2437, '6'),
('139', 'Hollywood', '6380 Hollywood Blvd', 'Los Angeles', 'CA', '90028', 'USA', '(323) 555-2345', 'hollywood@com', 'mgr_139', '2019-03-01', 3500.0, true, 34.1016, -118.3267, '6'),
('140', 'Venice Beach', '1800 Ocean Front Walk', 'Los Angeles', 'CA', '90291', 'USA', '(310) 555-3456', 'venice@com', 'mgr_140', '2017-08-01', 2800.0, false, 33.985, -118.4695, '6'),
('141', 'Silver Lake', '2800 Sunset Blvd', 'Los Angeles', 'CA', '90026', 'USA', '(323) 555-4567', 'silverlake@com', 'mgr_141', '2020-02-15', 3200.0, false, 34.0775, -118.2695, '6'),
('142', 'Echo Park', '1500 Echo Park Ave', 'Los Angeles', 'CA', '90026', 'USA', '(323) 555-5678', 'echopark@com', 'mgr_142', '2019-07-01', 2900.0, true, 34.0782, -118.2606, '6'),
('143', 'Los Feliz', '1800 N Vermont Ave', 'Los Angeles', 'CA', '90027', 'USA', '(323) 555-6789', 'losfeliz@com', 'mgr_143', '2018-09-15', 3400.0, false, 34.1044, -118.2919, '6'),
('144', 'Koreatown', '3500 W 6th St', 'Los Angeles', 'CA', '90020', 'USA', '(213) 555-7890', 'ktown@com', 'mgr_144', '2017-11-01', 3800.0, true, 34.0628, -118.3002, '6'),
('145', 'West LA', '11666 Olympic Blvd', 'Los Angeles', 'CA', '90064', 'USA', '(310) 555-8901', 'westla@com', 'mgr_145', '2020-01-15', 4000.0, false, 34.0379, -118.442, '6'),
('146', 'Studio City', '12345 Ventura Blvd', 'Los Angeles', 'CA', '91604', 'USA', '(818) 555-9012', 'studiocity@com', 'mgr_146', '2019-05-01', 3600.0, true, 34.1395, -118.3968, '6'),
('147', 'Culver City', '9800 Washington Blvd', 'Los Angeles', 'CA', '90232', 'USA', '(310) 555-0123', 'culvercity@com', 'mgr_147', '2018-04-15', 3300.0, false, 34.0211, -118.3965, '6'),

-- San Diego Area Stores
('148', 'Gaslamp Quarter', '614 5th Ave', 'San Diego', 'CA', '92101', 'USA', '(619) 555-1234', 'gaslamp@com', 'mgr_148', '2019-08-01', 3500.0, true, 32.7157, -117.1611, '6'),
('149', 'Pacific Beach', '4516 Mission Blvd', 'San Diego', 'CA', '92109', 'USA', '(619) 555-2345', 'pacificbeach@com', 'mgr_149', '2018-07-15', 3200.0, false, 32.7972, -117.2546, '6'),
('150', 'La Jolla', '7514 Girard Ave', 'San Diego', 'CA', '92037', 'USA', '(858) 555-3456', 'lajolla@com', 'mgr_150', '2017-12-01', 3800.0, true, 32.8473, -117.2742, '6'),
('151', 'North Park', '3000 University Ave', 'San Diego', 'CA', '92104', 'USA', '(619) 555-4567', 'northpark@com', 'mgr_151', '2020-03-15', 2900.0, false, 32.7483, -117.1295, '6'),
('152', 'Little Italy SD', '1735 India St', 'San Diego', 'CA', '92101', 'USA', '(619) 555-5678', 'littleitaly@com', 'mgr_152', '2019-06-01', 3400.0, true, 32.7223, -117.1687, '6'); 