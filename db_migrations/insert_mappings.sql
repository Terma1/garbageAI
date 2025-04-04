/*
-- Sample Data Inserts
INSERT INTO city_part (id, name) VALUES (1, 'Downtown'), (2, 'Suburb');

INSERT INTO street (id, name, city_part_id) VALUES (1, 'Main St', 1), (2, '2nd Ave', 2);

INSERT INTO garbage_type (id, name) VALUES (1, 'Plastic'), (2, 'Organic');

INSERT INTO state (id, name) VALUES (1, 'Pending'), (2, 'Collected');

INSERT INTO user_request (latitude, longitude, street_id, garbage_type, state, device_id, ip)
VALUES (40.7128, -74.0060, 1, 1, 1, 'Device123', '192.168.1.1');

INSERT INTO garbage_collection (garbage_type, street_id)
VALUES (1, 1);

INSERT INTO regulatory_data (garbage_type, city_part_id, garbage_collection_frequency_days_normal, garbage_collection_frequency_days_min, garbage_collection_frequency_days_max)
VALUES (1, 1, 7, 5, 10);
*/

INSERT INTO city_part (id, name) VALUES
(19935, 'Altstadt'),
(19936, 'Dürrbach alle mit Hafen'),
(19937, 'Frauenland'),
(19938, 'Grombühl'),
(19939, 'Heidingsfeld'),
(403107, 'Heuchelhof aussen'),
(403108, 'Heuchelhof innen'),
(19941, 'Lengfeld'),
(19942, 'Lindleinsmühle'),
(403103, 'Mainviertel'),
(506176, 'Neumühle'),
(401083, 'Pilziggrund'),
(19940, 'Rottenbauer'),
(19943, 'Sanderau'),
(19944, 'Steinbachtal'),
(19945, 'Versbach'),
(19946, 'Zellerau');

INSERT INTO street (id, name, city_part_id) VALUES
(19950, 'Abtsleitenweg', 19937),
(19951, 'Adalberostraße', 19943),
(19952, 'Adalbert-Stifter-Weg', 19944),
(19953, 'Adam-Güthlein-Straße', 19945),
(19954, 'Adelgundenweg', 19946),
(505731, 'Agnes-Sapper-Straße', 19937),
(19955, 'Ahornweg', 19941),
(19956, 'Akaziensteige', 19940),
(19957, 'Alandsgrund', 19937),
(19958, 'Albert-Balling-Gasse', 19939),
(19959, 'Albert-Einstein-Straße', 19936),
(19960, 'Albert-Günther-Weg', 19944),
(19961, 'Albert-Hoffa-Straße', 19937),
(19962, 'Albert-Schweitzer-Straße', 19941),
(19963, 'Albertsleitenweg', 19936),
(19964, 'Albertus-Magnus-Weg', 19942),
(19965, 'Alfons-M.-Mittnacht-Straße', 19941),
(19966, 'Alfred-Nobel-Straße', 19936),
(19967, 'Allendorfweg', 19939),
(19968, 'Allerseeweg', 19946),
(505734, 'Alte Fernstraße', 19937),
(19969, 'Alte Kasernstraße', 403103),
(19970, 'Alte Mainbrücke', 19935),
(19972, 'Alter Bergweg', 19936),
(19971, 'Alte Würzburger Straße', 19941),
(20034, 'Amalienstraße', 19943),
(19973, 'Am Altenberg', 19945),
(505739, 'Am Alten Flugfeld', 19937),
(19974, 'Am Bauhof', 19941),
(19975, 'Am Baumland', 19940),
(19976, 'Am Blosenberg', 19944),
(19977, 'Am Bruderhof', 19935),
(403109, 'Am Brunnen', 19940),
(19978, 'Am Brünnlein', 19940),
(19979, 'Am Dicken Turm', 403103),
(19980, 'Am Dürrbach', 19936),
(19981, 'Am Eselsbach', 19945),
(19982, 'Am Exerzierplatz', 19943),
(19983, 'Am Feldkreuz', 19940),
(19984, 'Am Galgenberg', 19937),
(19985, 'Am Geisberg', 19939),
(19986, 'Am Glitzelberg', 19936),
(19987, 'Am Greinberg', 19938),
(19988, 'Am Handelshof', 19941),
(19989, 'Am Hasensprung', 19941),
(19990, 'Am Heigelsbach', 19939),
(19991, 'Am Heuchel', 19940),
(19992, 'Am Hölzlein', 19941),
(19993, 'Am Hubland', 19937),
(19994, 'Am Hungrigen Bühl', 19939),
(19995, 'Am Kalkofen', 19944),
(19996, 'Am Klößberg', 19944),
(19997, 'Am Kugelfang', 19937),
(19998, 'Am Kuhberg', 19936),
(19999, 'Am Mühlenhang', 19941),
(20000, 'Am Nikolausspital', 19939),
(20001, 'Am Nikolaustor', 19939),
(20002, 'Am Ostbahnhof', 19939),
(20003, 'Am Pfaffenberg', 19936),
(20004, 'Am Pfaffenrain', 403107),
(20005, 'Am Pleidenturm', 19935),
(20006, 'Am Reuschert', 403107),
(20007, 'Am Roßberg', 19936),
(20008, 'Am Rubenland', 19939),
(20009, 'Am Salmannsturm', 19939),
(20010, 'Am Sand', 19936),
(20011, 'Am Schaftrieb', 19936),
(20012, 'Am Schellengraben', 403107),
(20013, 'Am Schenkenturm', 19936),
(20014, 'Am Schießgraben', 19941),
(20015, 'Am Schloß', 19940),
(20016, 'Am Schloßgarten', 19941),
(20017, 'Am Schwarzenberg', 506176),
(20018, 'Am Sonnenberg', 19945),
(20019, 'Am Sonnenhof', 19941),
(20020, 'Am Sonnfeld', 19941),
(20021, 'Am Stadtberg', 19945),
(20022, 'Am Steg', 19945),
(20023, 'Am Stein', 19938),
(20024, 'Am Stockbrunnen', 19940),
(20026, 'Am Stuck', 401083),
(20027, 'Am Studentenhaus', 19943),
(505729, 'Am Terrassenpark', 19937),
(20028, 'Am Trog', 401083),
(20029, 'Am Wald', 19944),
(20030, 'Am Wandberg', 19936),
(20031, 'Am Weinberg', 19941),
(20032, 'Am Westbahnhof', 19939),
(20033, 'Am Zehentfreien', 19945),
(20035, 'An den Breiten', 19945),
(20036, 'An den drei Pappeln', 19944),
(20037, 'An den Mühltannen', 19936),
(20038, 'An den Röthen', 19936),
(20039, 'An der Jahnhöhe', 19939),
(20040, 'An der Linde', 19945),
(20041, 'An der Löwenbrücke', 19935),
(20042, 'An der Pleichach', 19945),
(20043, 'An der Stadtmauer', 19939),
(20044, 'An der Steige', 19936),
(20045, 'An der Sternwarte', 19937),
(20046, 'Andreas-Grieser-Straße', 19939),
(20047, 'Anemonenweg', 19940),
(20330, 'Angermaierstraße', 401083),
(20048, 'Annaschlucht', 19944),
(20049, 'Annastraße', 19935),
(20050, 'Anne-Frank-Straße', 19944),
(20051, 'Anton-Bruckner-Straße', 19937),
(20052, 'Antonie-Werr-Straße', 19946),
(20053, 'Antonius-Lauck-Straße', 19939),
(20054, 'Armin-Knab-Straße', 19937),
(20055, 'Arndtstraße', 19943),
(20056, 'Artztlade', 19935),
(505727, 'Athanasius-Kircher-Straße', 19937),
(20057, 'Athener Ring', 403107),
(20058, 'Auf der Läng', 19941),
(20059, 'Auf der Röthe', 19941),
(20060, 'Auf der Schanz', 19941),
(20061, 'Augustinerstraße', 19935),
(20062, 'August-Sperl-Straße', 19937),
(20063, 'Äußere Aumühlstraße', 19938),
(20064, 'Äußerer Hublandweg', 19937),
(20065, 'Äußerer Neubergweg', 19937),
(20066, 'Äußerer Tränkeweg', 19937),
(20067, 'Auverastraße', 19938),
(20068, 'Bachgasse', 19935),
(20069, 'Badergasse', 19935),
(20070, 'Bahnhofplatz', 19935),
(20071, 'Bahnhofstraße', 19935),
(20072, 'Balthasar-Neumann-Promenade', 19935),
(20073, 'Banatstraße', 19945),
(20074, 'Barbarastraße', 19937),
(20075, 'Barbarossaplatz', 19935),
(20076, 'Bärengasse', 19935),
(20077, 'Bauernpfad', 19939),
(20078, 'Bauerstraße', 19936),
(20079, 'Bayernstraße', 19942),
(20080, 'Beethovenstraße', 19935),
(20081, 'Behrstraße', 19937),
(20082, 'Bei der Neumühle', 506176),
(20083, 'Beim Grafeneckart', 19935),
(20084, 'Belgrader Straße', 403107),
(20085, 'Bentheimstraße', 19943),
(20086, 'Benzstraße', 19946),
(20087, 'Berggasse', 19939),
(20088, 'Bergmeistergasse', 19935),
(20089, 'Bergstraße', 19941),
(20090, 'Berlichingenstraße', 19939),
(20091, 'Berliner Platz', 19935),
(20092, 'Berner Straße', 403107),
(20093, 'Betpfad', 19944),
(20094, 'Bibrastraße', 19935),
(20095, 'Birkenhain', 19936),
(20096, 'Birkenstraße', 19941),
(20097, 'Bismarckstraße', 19935),
(20098, 'Blasiusgasse', 19935),
(20099, 'Blöhlein', 19935),
(20100, 'Blosenbergpfad', 19939),
(20101, 'Blosenbergweg', 19939),
(20102, 'Bockgasse', 19935),
(20103, 'Bockspfad', 19938),
(20104, 'Bodelschwingstraße', 19937),
(20105, 'Bohlleitenweg', 19946),
(20106, 'Bohnesmühlgasse', 19935),
(20107, 'Bonhoefferstraße', 19945),
(20108, 'Bonner Straße', 403108),
(20109, 'Bossistraße', 19938),
(20111, 'Breite Länge', 19945),
(20112, 'Bremenweg', 19939),
(20113, 'Breslauer Straße', 19943),
(20114, 'Brettreichstraße', 19937),
(20115, 'Brombergweg', 19940),
(20116, 'Bronnbachergasse', 19935),
(20117, 'Bronnbacherhof', 19935),
(20118, 'Brücknerstraße', 19938),
(20119, 'Brunnenstraße', 19945),
(20120, 'Brunnfloßgasse', 19945),
(20121, 'Brunostraße', 19946),
(20122, 'Brüsseler Straße', 403108),
(20123, 'Buchengraben', 19936),
(20124, 'Buchenweg', 19941),
(20125, 'Budapester Straße', 403107),
(20126, 'Bukarester Straße', 403107),
(20127, 'Bürgermeister-Otto-Straße', 19939),
(20128, 'Burkarderstraße', 403103),
(20129, 'Büttnerstraße', 19935),
(20130, 'Carl-Orff-Straße', 19941),
(20131, 'Christelsteige', 19937),
(20132, 'Christoph-Mayer-Weg', 19944),
(20133, 'Conradistraße', 19943),
(20134, 'Crevennastraße', 19935),
(20135, 'Cronthalstraße', 19937),
(20136, 'Daimlerstraße', 19946),
(20137, 'Damaschkestraße', 19937),
(20138, 'Danziger Straße', 19943),
(20139, 'Delphiweg', 403107),
(20140, 'Delpstraße', 403107),
(20141, 'Den Haager Straße', 403108),
(20142, 'Dettelbachergasse', 19935),
(20143, 'Dieselstraße', 19946),
(20144, 'Dollgasse', 19939),
(20145, 'Domerpfarrgasse', 19935),
(20146, 'Domerschulstraße', 19935),
(20147, 'Dominikanergasse', 19935),
(20148, 'Dominikanerplatz', 19935),
(20149, 'Domstraße', 19935),
(20150, 'Domweg', 19939),
(20151, 'Dorfäcker', 19940),
(20152, 'Dorfgraben', 19941),
(20153, 'Dorfplatz', 19936),
(20154, 'Dornröschenweg', 19939),
(20158, 'Dreikronenstraße', 403103),
(505726, 'Dr.-Georg-Fuchs-Straße', 19937),
(506072, 'Dr.-Georg-Teichtweier-Straße', 19941),
(20155, 'Dr.-Heinrich-Wunderlich-Str.', 19941),
(20159, 'Dritte Felsengasse', 403103),
(403122, 'Dr.-Johanna-Stahl-Straße', 403107),
(20156, 'Dr.-Maria-Probst-Straße', 19946),
(20157, 'Dr.-Onymus-Straße', 19936),
(20160, 'Dubliner Straße', 403107),
(20161, 'Dundeestraße', 403107),
(20162, 'Dürerstraße', 19935),
(20163, 'Dürrbachtal', 19936),
(20164, 'Dürrenberg', 19939),
(20165, 'Ebertsklinge', 19937),
(20166, 'Ebrachergasse', 19935),
(20167, 'Eckleinsweg', 19939),
(20168, 'Edelstraße', 19937),
(20169, 'Edith-Stein-Straße', 403107),
(20170, 'Eduard-Buchner-Straße', 19936),
(20171, 'Egloffsteinstraße', 19943),
(20172, 'Eibelstadter Weg', 19940),
(403111, 'Eibenweg', 19940),
(20173, 'Eichendorffstraße', 19943),
(403110, 'Eichenweg', 19940),
(20174, 'Eichhornstraße', 19935),
(20175, 'Eichstraße', 19935),
(20176, 'Eisenbahnstraße', 19939),
(20177, 'Eiseneckstraße', 19946),
(20178, 'Eisenhoferstraße', 19937),
(20179, 'Eisenmannstraße', 19937),
(20180, 'Elefantengasse', 19935),
(20181, 'Elferweg', 19937),
(505730, 'Elisabeth-Scheuring-Straße', 19937),
(20182, 'Ellernweg', 19936),
(20599, 'Elli-Michler-Straße', 19939),
(20183, 'Elstergasse', 403103),
(20184, 'Emy-Roeder-Straße', 19937),
(20185, 'Engelsweg', 19940),
(20186, 'Enzelinstraße', 19938),
(20187, 'Ephesusweg', 403107),
(20188, 'Erlenweg', 19941),
(20189, 'Ernst-Reuter-Straße', 19938),
(20190, 'Ernst-Winter-Weg', 19940),
(20191, 'Erste Felsengasse', 403103),
(20192, 'Erster Siedlungsweg', 19946),
(20193, 'Erthalstraße', 19937),
(20194, 'Erzherzog-Karl-Platz', 19937),
(20195, 'Eschenweg', 19940),
(20196, 'Essiggarten', 19941),
(20197, 'Essigkrug', 19945),
(20198, 'Estenfelder Straße', 19945),
(20199, 'Eulensteige', 19944),
(20200, 'Europastern', 19938),
(20201, 'Falkenstraße', 19941),
(20202, 'Faribaultstraße', 403107),
(20203, 'Fasanenstraße', 19941),
(20204, 'Fasbenderstraße', 19946),
(20205, 'Faulenbergstraße', 19938),
(20206, 'Fechenbachstraße', 19943),
(20207, 'Feggrube', 19943),
(20208, 'Felix-Dahn-Straße', 19943),
(20209, 'Ferdinand-Nickles-Straße', 401083),
(505732, 'Ferdinand-Tietz-Straße', 19937),
(20210, 'Fichtestraße', 19937),
(20211, 'Finkenweg', 19944),
(20212, 'Fischleingasse', 19939),
(20213, 'Florastraße', 19943),
(20214, 'Floraweg', 19943),
(20215, 'Florian-Geyer-Straße', 19941),
(20216, 'Flürleinstraße', 19941),
(20217, 'Frankenlandstraße', 19941),
(20218, 'Frankenstraße 1-197 ung./2-210 ger. Nr.', 19942),
(20219, 'Frankenstraße 212-Ende ger./199-Ende ung. Nr.', 19945),
(20220, 'Frankenwarte', 19944),
(20221, 'Frankfurter Straße', 19946),
(505728, 'Franz-Brentano-Straße', 19937),
(20222, 'Franz-Bretz-Straße', 19939),
(20223, 'Franz-Horn-Straße', 19946),
(20224, 'Franziskanergasse', 19935),
(20225, 'Franziskanerplatz', 19935),
(20226, 'Franz-Liszt-Straße', 19937),
(20227, 'Franz-Ludwig-Straße', 19943),
(20228, 'Franzosenweg', 19944),
(20229, 'Franz-Schubert-Straße', 19937),
(20230, 'Franz-Stadelmayer-Straße', 19937),
(20231, 'Frauenlandplatz', 19937),
(20232, 'Frauenlandstraße', 19937),
(20233, 'Frau-Holle-Weg', 19939),
(20234, 'Fraunhoferstraße', 19938),
(20235, 'Friedenstraße', 19943),
(20236, 'Friedhofstraße', 19940),
(20237, 'Friedrich-Bergius-Ring', 19938),
(20238, 'Friedrich-Ebert-Ring 1-12', 19935),
(20239, 'Friedrich-Ebert-Ring ab 13', 19943),
(20240, 'Friedrich-Fick-Straße', 19937),
(20241, 'Friedrich-Koenig-Straße', 19936),
(20242, 'Friedrich-Kohlrausch-Straße', 19936),
(20243, 'Friedrich-Spee-Straße', 19943),
(20244, 'Friedrichstraße', 19946),
(20245, 'Friesstraße', 19937),
(20246, 'Fritz-Erler-Straße', 19941),
(20247, 'Fritz-Haber-Straße', 19936),
(20248, 'Fröbelstraße', 19937),
(20249, 'Fröhlichstraße', 19946),
(20250, 'Frühlingstraße', 19941),
(20251, 'Fuchsgasse', 19939),
(20252, 'Füchsleinstraße', 19938),
(20253, 'Gabelsbergerstraße', 19938),
(20254, 'Gadheimer Straße', 19936),
(20255, 'Gänsleinsweg', 19946),
(20256, 'Gartenstraße', 19943),
(20257, 'Gattingerstraße', 19938),
(20258, 'Gebr.-Grimm-Straße', 19945),
(20259, 'Gegenbaurstraße', 19937),
(20260, 'Geibelstraße', 19943),
(20261, 'Geisberg', 19939),
(20262, 'Geisberggraben', 19939),
(20263, 'Georg-Böhm-Straße', 19938),
(20264, 'Georg-Engel-Straße', 19941),
(20265, 'Georg-Eydel-Straße', 19946),
(20266, 'Georg-Sittig-Straße', 19937),
(20267, 'Gerberstraße', 19935),
(20268, 'Gerbrunner Weg', 19937),
(505735, 'Gerda-Laufer-Straße', 19937),
(20269, 'Gertraudgasse', 19935),
(20270, 'Gertraud-Rostosky-Straße', 19944),
(20271, 'Gertrud-von-le-Fort-Straße', 19937),
(20272, 'Geschwister-Scholl-Platz', 19935),
(20273, 'Giebelstädter Steige', 403107),
(20274, 'Glacisweg', 19939),
(20275, 'Glockengasse', 19935),
(20276, 'Gneisenaustraße', 19937),
(20277, 'Göbelslehenstraße', 19937),
(20278, 'Goerdelerstraße', 403107),
(20279, 'Goethestraße', 19935),
(20280, 'Goldbergstraße', 19945),
(20281, 'Gosbertsteige', 19946),
(20282, 'Gotengasse', 19935),
(20283, 'Grabenberg', 19935),
(20284, 'Grabengasse', 19935),
(20285, 'Graf-Luckner-Weiher', 19943),
(20286, 'Grasweg', 19937),
(20287, 'Greiffenclaustraße', 19943),
(20288, 'Greisingstraße', 19937),
(20289, 'Gressengasse', 19935),
(20290, 'Griesäckerstraße', 19945),
(20291, 'Grillparzerstraße', 19943),
(20292, 'Grombühlstraße', 19938),
(20293, 'Grundäckerstraße', 19936),
(20294, 'Grünewaldstraße', 19935),
(20295, 'Guggelesgraben', 19944),
(20296, 'Gulbranssonstraße', 19946),
(20297, 'Gutenbergstraße', 19938),
(20298, 'Gutental', 19937),
(20299, 'Güterbahnhof Zell', 19936),
(20300, 'Guttenbergerstraße', 19944),
(20301, 'Haafstraße', 19946),
(20302, 'Hackstetterstraße', 19937),
(20303, 'Häfnergasse', 19935),
(20304, 'Hahnenhof', 19935),
(20305, 'Händelstraße', 19937),
(20306, 'Handgasse', 19935),
(20307, 'Hans-Brandmann-Weg', 19938),
(20308, 'Hans-Löffler-Straße', 19937),
(20309, 'Hans-Sachs-Weg', 19944),
(20310, 'Harfenstraße', 19935),
(20311, 'Hartmannstraße', 19946),
(20312, 'Haugerglacisstraße', 19935),
(20313, 'Haugerkirchgasse', 19935),
(20314, 'Haugerkirchplatz', 19935),
(20315, 'Haugerpfarrgasse', 19935),
(20316, 'Haugerring', 19935),
(20317, 'Häuselsberg', 19938),
(20318, 'Haydnstraße', 19937),
(20319, 'Hebbelstraße', 19943),
(20320, 'Hedanstraße', 19939),
(20321, 'Heide', 19945),
(20322, 'Heidingsfelder Weg', 403107),
(20323, 'Heimgartenweg', 19937),
(20325, 'Heinestraße', 19935),
(20326, 'Heinrichsleitenweg', 19936),
(20327, 'Heinrich-Zeuner-Straße', 19944),
(20328, 'Heisenbergstraße', 19941),
(20329, 'Heißberg', 19944),
(20331, 'Helsinkistraße', 403107),
(20332, 'Henlestraße', 19937),
(20333, 'Heriedenweg', 19939),
(20334, 'Hermann-Löns-Weg', 19944),
(20335, 'Hermann-Mitnacht-Straße', 19941),
(20336, 'Hermann-Schell-Straße', 19937),
(20338, 'Hermann-Zürrlein-Str.', 19941),
(20339, 'Herrnhofstraße', 19941),
(20340, 'Herrnstraße', 19935),
(20341, 'Herta-Mannheimer-Weg', 19939),
(20342, 'Hertzstraße', 19938),
(20343, 'Herzogenstraße', 19935),
(20344, 'Hessenstraße', 19942),
(20345, 'Heuchelhofstraße', 403107),
(20346, 'Hexenbruchweg', 19946),
(20347, 'Hintere Heuchel', 19940),
(20348, 'Hintere Kirchgasse', 19945),
(20349, 'Hinterer Johannishof', 19944),
(20350, 'Hinterer Kirchbergweg', 19939),
(20351, 'Hinterer Kühlenberg', 19945),
(20352, 'Hinteres Steinbachtal', 19944),
(20353, 'Hirschberger Straße', 19943),
(20354, 'Hirschleinstraße', 19936),
(20355, 'Höchberger Straße', 19946),
(20356, 'Hoffeldäcker', 19940),
(20357, 'Hofleitenweg', 19936),
(20358, 'Hofmannstraße', 19939),
(20359, 'Hofmeierstraße', 19937),
(20360, 'Hofstallstraße', 19935),
(20361, 'Hofstraße', 19935),
(20363, 'Hoher Weg', 19944),
(20362, 'Hohe Steige', 403107),
(20364, 'Holunderweg', 19940),
(20365, 'Holzbühlweg', 19937),
(20366, 'Hölzlesweg', 19938),
(20367, 'Holztorgasse', 19935),
(20368, 'Holzweg', 19939),
(20369, 'Hopfenberg', 19936),
(20370, 'Hörleingasse', 19935),
(20371, 'Huberstraße', 403107),
(20372, 'Hubertistraße', 19937),
(20373, 'Hubertusschlucht', 19944),
(20374, 'Hubertusweg', 19944),
(505725, 'Hublandplatz', 19937),
(20375, 'Huebergasse', 19935),
(20376, 'Hunsingerweg', 19939),
(20377, 'Husarenstraße', 19935),
(20378, 'Huttenstraße', 19943),
(20379, 'Hüttenweg', 19936),
(506025, 'Ilse-Totzke-Straße', 19937),
(20380, 'Im Grund', 19936),
(20381, 'Im Hirschlein', 19936),
(20382, 'Im Hubland', 19937),
(20383, 'Im Kreuz', 19938),
(20384, 'Industriestraße', 19941),
(20385, 'Ingolstadter Hof', 19935),
(20386, 'Innere Aumühlstraße', 19938),
(20387, 'Innerer Graben', 19935),
(20388, 'Innerer Hublandweg', 19937),
(20389, 'Jägerruh', 19941),
(20390, 'Jägerstraße', 19946),
(20391, 'Jahnstraße', 19941),
(20392, 'Jakob-Riedinger-Straße', 19937),
(20393, 'Johannes-Kepler-Straße', 19937),
(20394, 'Johann-Herrmann-Straße', 19945),
(20395, 'Johannisweg', 19944),
(20396, 'Johanniterplatz', 19935),
(20397, 'Johanniterweg', 19941),
(20398, 'Johann-Salomon-Straße', 19936),
(20399, 'Johann-Sperl-Straße', 19935),
(505736, 'John-Skilton-Straße', 19937),
(20400, 'Josefplatz', 19938),
(20401, 'Josef-Schneider-Straße', 19938),
(20402, 'Josef-Stangel-Platz', 19935),
(20403, 'Josefstraße', 19938),
(20404, 'Joseph-Seitz-Straße', 401083),
(20405, 'Judenbühlweg', 19944),
(20406, 'Judenhof', 19939),
(20407, 'Judenplan', 19939),
(20408, 'Julius-Echter-Straße', 19939),
(20409, 'Juliuspromenade', 19935),
(20410, 'Kaiserplatz', 19935),
(20411, 'Kaiserstraße', 19935),
(20412, 'Kantstraße', 19937),
(20413, 'Käppele', 19944),
(20414, 'Kapuzinerstraße', 19935),
(20415, 'Kardinal-Döpfner-Platz', 19935),
(20416, 'Kardinal-Faulhaber-Platz', 19935),
(20417, 'Karl-Ferdinant-Braun-Straße', 19936),
(20418, 'Karl-Pfetscher-Weg', 19944),
(20419, 'Karl-Ritter-von-Frisch-Weg', 19937),
(20420, 'Karl-Straub-Straße', 19939),
(20421, 'Karmelitenstraße', 19935),
(20422, 'Kärrnergasse', 19935),
(20423, 'Kartause', 19935),
(20424, 'Kastanienstraße', 19940),
(20425, 'Katharinengasse', 19935),
(20426, 'Katzengasse', 403103),
(20427, 'Kaulstraße', 19939),
(20428, 'Keesburgstraße', 19937),
(20430, 'Keltenstraße', 19941),
(20431, 'Kettelerstraße', 19937),
(20432, 'Kettengasse', 19935),
(20433, 'Kiefernweg', 19940),
(20434, 'Kieseläckerweg', 19939),
(20435, 'Kiliansplatz', 19935),
(20436, 'Kirchbühlstraße', 19937),
(20437, 'Kirchgasse', 19939),
(20438, 'Kirchhofstraße', 19939),
(20439, 'Kirchplatz', 19939),
(403112, 'Kirschbaumweg', 19940),
(20440, 'Kittelstraße', 19937),
(20441, 'Klara-Löwe-Straße', 19944),
(403113, 'Kleines Flürlein', 19940),
(20442, 'Kleiststraße', 19943),
(20443, 'Kleßbergsteige', 19944),
(20444, 'Kliebertstraße', 19935),
(20445, 'Klingenstraße', 19939),
(20446, 'Klingenweg', 19936),
(20447, 'Klinikstraße', 19935),
(20448, 'Klopfergasse', 19939),
(20449, 'Klostergasse', 19935),
(20450, 'Klosterstraße', 19939),
(20451, 'Kniebreche', 19944),
(20452, 'Köchleinsweg', 19939),
(20453, 'Koellikerstraße', 19935),
(20454, 'Kohlenhofstraße', 19935),
(20455, 'Kolonieweg', 19939),
(20456, 'Kolpingstraße', 19935),
(20457, 'König-Heinrich-Straße', 19944),
(20458, 'Königsberger Straße', 19943),
(20459, 'Konradstraße', 19935),
(20462, 'Kopenhagener Straße', 403107),
(20460, 'Koppberggraben', 19936),
(20461, 'Koppbergweg', 19936),
(20463, 'Korngasse', 19935),
(20464, 'Kranenkai', 19935),
(20465, 'Krautäckerstraße', 19936),
(20466, 'Kreuzbergstraße', 19936),
(20467, 'Kroatengasse', 19935),
(20468, 'Kronbergstraße', 19945),
(20469, 'Kühlenbergstraße', 19945),
(20470, 'Kürnachtalstraße', 19941),
(20471, 'Kürschner Hof', 19935),
(20472, 'Kurze Gasse', 19941),
(505740, 'Landsteinerstraße', 19937),
(20473, 'Landwehrstraße', 19935),
(20474, 'Lange Bögen', 19937),
(20475, 'Langer Weg', 19936),
(20476, 'Langes Gräthlein', 19945),
(20477, 'Langgasse', 19935),
(20478, 'Lärchenweg', 19940),
(20479, 'Laufergasse', 403103),
(20480, 'Laurentiusstraße', 19941),
(20481, 'Lehmgrubenweg', 19939),
(20482, 'Lehnleitenweg', 19937),
(20483, 'Leiblstraße', 19935),
(505737, 'Leightonstraße', 19937),
(20484, 'Leistenstraße', 19944),
(20485, 'Leitenäckerweg', 19939),
(20486, 'Leitengraben', 19939),
(20487, 'Leitenpfad', 19944),
(20488, 'Lendnerstraße', 19937),
(404556, 'Lengfelder Höh', 19941),
(506723, 'Lengfelder Landwehr', 19941),
(20489, 'Lengfelder Straße', 19945),
(20490, 'Leonhard-Frank-Promenade', 19946),
(20491, 'Leo-Weismantel-Straße', 19937),
(20492, 'Lerchenhain', 19937),
(20493, 'Lerchenweg', 19937),
(20494, 'Lessingstraße', 19943),
(20495, 'Leubestraße', 19937),
(20496, 'Leuschnerstraße', 403107),
(20497, 'Leutfresserweg', 19944),
(20498, 'Liborius-Wagner-Straße', 19941),
(20499, 'Liebigstraße', 19936),
(20500, 'Liegnitzer Straße', 19943),
(20501, 'Lilienweg', 19940),
(20502, 'Lindachfeldweg', 19938),
(20503, 'Lindahlstraße', 19935),
(20504, 'Lindenstraße', 19940),
(20505, 'Lindflurer Straße', 19940),
(20506, 'Lindleinstraße', 19938),
(20507, 'Lindleshang', 19938),
(403114, 'Linsen', 19940),
(20508, 'Lissabonner Straße', 403107),
(20509, 'Löffelgasse', 19939),
(20510, 'Londoner Straße', 403107),
(20511, 'Lortzingstraße', 19937),
(506715, 'Lothar-Forster-Straße', 19936),
(20512, 'Louis-Pasteur-Straße', 19938),
(20513, 'Ludwigkai', 19943),
(20514, 'Ludwigstraße', 19935),
(20515, 'Ludwig-Weis-Straße', 19946),
(20516, 'Luitpoldgraben', 19936),
(20517, 'Luitpoldquelle', 19936),
(20518, 'Luitpoldstraße', 19946),
(20519, 'Luxemburger Straße', 403108),
(20520, 'Maasweg', 19944),
(20521, 'Madrider Ring', 403107),
(505741, 'Magdalena-Schoch-Straße', 19937),
(403115, 'Mageritenweg', 19940),
(20522, 'Maidbronner Weg', 19945),
(20523, 'Maiergasse', 19935),
(20524, 'Maillingerstraße', 19946),
(20525, 'Mainaustraße', 19946),
(20526, 'Maingäßchen', 19937),
(20527, 'Maingasse', 19939),
(20528, 'Mainkai', 19935),
(20529, 'Mainleitenweg', 19944),
(20530, 'Malterserweg', 19941),
(20531, 'Mandelbaumweg', 19940),
(20532, 'Marcusstraße', 19935),
(20533, 'Marianhillstraße', 19937),
(20534, 'Maria-Theresia-Promenade', 19944),
(20535, 'Marienberg', 19946),
(20536, 'Marienplatz', 19935),
(20537, 'Marienstraße', 19935),
(20538, 'Marktgasse', 19935),
(20539, 'Marktplatz', 19935),
(20540, 'Martin-Luther-Straße', 19935),
(20541, 'Martinstraße', 19935),
(20542, 'Matterstockstraße', 19938),
(20543, 'Matthias-Ehrenfried-Straße', 19937),
(20544, 'Matthias-Noell-Weg', 19939),
(20545, 'Maulhardgasse', 19935),
(20546, 'Maurmeierstraße', 19937),
(20547, 'Max-Born-Straße', 19936),
(20548, 'Max-Dauthendey-Straße', 19943),
(20549, 'Max-Heim-Straße', 19937),
(403116, 'Maximilian-Kolbe-Strasse', 19940),
(506006, 'Max-Mengeringhausen-Straße', 403107),
(20551, 'Max-Planck-Straße', 19946),
(20552, 'Max-Reger-Straße', 19937),
(20553, 'Max-Schnabel-Straße', 19939),
(20554, 'Maxstraße', 19935),
(20555, 'Max-von-Laue-Straße', 19936),
(20556, 'Meisenweg', 19944),
(20558, 'Mergentheimer Straße 1-21 ung./4-110 ger. Nr.', 19944),
(20557, 'Mergentheimer Straße  23-Ende ung./112-Ende ger. Nr.', 19939),
(20559, 'Methfesselstraße', 19937),
(20560, 'Meyer-Olbersleben-Straße', 19937),
(20561, 'Michael-Brand-Straße', 19945),
(20562, 'Michelstraße', 19946),
(20563, 'Miletweg', 403107),
(20324, 'Milly-Marbe-Fries-Weg', 19943),
(20564, 'Mittlere Heerbergstraße', 19945),
(20565, 'Mittlerer Dallenbergweg', 19944),
(20566, 'Mittlerer Greinbergweg', 19938),
(20567, 'Mittlerer Katzenbergweg', 19939),
(20568, 'Mittlerer Kirchbergweg', 19939),
(20569, 'Mittlerer Neubergweg', 19937),
(20570, 'Mittlerer Schalksbergweg', 19938),
(20571, 'Mittlerer Steinbachweg', 19944),
(20572, 'Mittlerer Steinbergweg', 19938),
(20573, 'Mittlerer Wiesenweg', 19936),
(20574, 'Mohnstraße', 19936),
(20575, 'Moltkestraße', 19946),
(20576, 'Mönchbergstraße', 19937),
(20577, 'Mönchsgartenweg', 19939),
(20578, 'Morellistraße', 19938),
(20579, 'Moritzgasse', 19935),
(20580, 'Moscheeweg', 19946),
(20581, 'Moskauer Ring', 403107),
(20582, 'Mozartstraße', 19937),
(20583, 'Mühlenstraße', 19939),
(20584, 'Mühlweg', 19945),
(20585, 'Münchgasse', 19939),
(20586, 'Münzstraße', 19935),
(403120, 'Mwanzaweg', 403107),
(20587, 'Nachtigallenweg', 19937),
(20588, 'Neidertstraße', 19946),
(20589, 'Nelkenweg', 19940),
(20590, 'Neubaustraße', 19935),
(20591, 'Neubergstraße', 19943),
(20592, 'Neuenberg', 19936),
(20593, 'Neuenbrunner Weg', 19936),
(20594, 'Neuer Hafen', 19936),
(20595, 'Neunerplatz', 19946),
(20596, 'Neutorstraße', 19935),
(20597, 'Neydeckgasse', 403103),
(20598, 'Nigglweg', 403103),
(20600, 'Nikolausstraße', 19944),
(20601, 'Nopitschstraße', 19937),
(505733, 'Norbert-Glanzberg-Straße', 19937),
(20602, 'Nördliche Hafenstraße', 19936),
(20603, 'Nürnberger Straße', 19938),
(20604, 'Nußbaumweg', 19940),
(20605, 'Oberdürrbacher Straße', 19938),
(20606, 'Obere Heerbergstraße', 19945),
(20607, 'Obere Hofgasse', 19945),
(20608, 'Obere Johannitergasse', 19935),
(20610, 'Oberer Adelbergweg', 19945),
(20611, 'Oberer Bogenweg', 19937),
(20612, 'Oberer Burgweg', 19946),
(20613, 'Oberer Dallenbergweg', 19944),
(20614, 'Oberer Geibergweg', 19939),
(20615, 'Oberer Katzenbergweg', 19939),
(20616, 'Oberer Kirchbergweg', 19939),
(20617, 'Oberer Kirchplatz', 19940),
(20618, 'Oberer Kühlenberg', 19945),
(20619, 'Oberer Leitenweg', 19944),
(20620, 'Oberer Mainkai', 19935),
(20621, 'Oberer Neubergweg', 19937),
(20622, 'Oberer Schalksbergweg', 19938),
(20623, 'Oberer Steinbachweg', 19944),
(20624, 'Oberer Steinbergweg', 19936),
(20625, 'Oberer Torweinberg', 19940),
(20609, 'Obere Wand', 19936),
(20626, 'Oberhofstraße', 19936),
(20627, 'Oberthürstraße', 19935),
(20628, 'Odenwaldstraße', 19941),
(20629, 'Oeggstraße', 19935),
(20630, 'Öhlberg', 19936),
(20631, 'Ohmstraße', 19938),
(20632, 'Olympia-Promenade', 403107),
(20633, 'Osloer Straße', 403107),
(20634, 'Ossietzkystraße', 403107),
(20635, 'Ostpreußenstraße', 19942),
(20636, 'Otsustraße', 403107),
(20637, 'Otto-Fritz-Straße', 19939),
(20638, 'Otto-Hahn-Straße', 19936),
(20639, 'Otto-Nagler-Straße', 19937),
(20640, 'Otto-Richter-Straße', 19937),
(20641, 'Otto-Roth-Straße', 19941),
(20642, 'Otto-Stein-Straße', 401083),
(20643, 'Ottostraße', 19935),
(20644, 'Pacotistraße', 19941),
(20645, 'Paradeplatz', 19935),
(20646, 'Paradieshof', 19936),
(20647, 'Paradiesstraße', 19936),
(20648, 'Pariser Straße', 403108),
(20649, 'Parsevalstraße', 19937),
(20650, 'Pergamonweg', 403107),
(20651, 'Pestalozzistraße', 19938),
(20652, 'Peter-Haupt-Straße', 19936),
(20653, 'Peterpfarrgasse', 19935),
(20654, 'Peterplatz', 19935),
(20655, 'Peter-Schneider-Straße', 19937),
(20656, 'Peterstraße', 19935),
(20657, 'Peter-Wagner-Straße', 19936),
(20658, 'Petrinistraße', 19938),
(20659, 'Pfaffenbergstraße', 19936),
(20660, 'Pfaffenbergweg', 19936),
(20661, 'Pfalzstraße', 19942),
(20662, 'Pfarrer-Paul-Nützel-Straße', 19946),
(20663, 'Pfauengasse', 19935),
(20664, 'Philipp-Fasel-Str.', 19941),
(20665, 'Pickelstraße', 19935),
(20666, 'Pilziggrundstraße', 401083),
(20667, 'Place de Caen', 403108),
(20668, 'Platenstraße', 19943),
(20669, 'Plattnerstraße', 19935),
(20670, 'Pleichachgrund', 19945),
(20671, 'Pleicherkirchgasse', 19935),
(20672, 'Pleicherkirchplatz', 19935),
(20673, 'Pleicherpfarrgasse', 19935),
(20674, 'Pleicherschulgasse', 19935),
(20675, 'Pleichertorstraße', 19935),
(20676, 'Pleicherwall', 19935),
(20677, 'Pommergasse', 19935),
(20678, 'Popspfad', 19937),
(20679, 'Prager Ring', 403107),
(20680, 'Prymstraße', 19935),
(20681, 'Rabanus-Maurus-Straße', 19941),
(20682, 'Radulfsteige', 19946),
(20683, 'Raiffeisenstraße', 19935),
(20684, 'Randersackerer Straße', 19943),
(20685, 'Randersackerer Weg', 19939),
(20686, 'Rathausplatz Heidingsfeld', 19939),
(20687, 'Rebenstraße', 19940),
(20688, 'Reibeltgasse', 19935),
(20689, 'Reichenberger Straße', 403107),
(20690, 'Reiserstraße', 19938),
(20691, 'Reisgrubengasse', 19935),
(20692, 'Rembrandtstraße', 19941),
(20693, 'Rennweg', 19935),
(20694, 'Rennweger Ring', 19935),
(20695, 'Resenstraße', 19939),
(20696, 'Resenweg', 19939),
(20697, 'Residenzplatz', 19935),
(20698, 'Reuerergasse', 19935),
(20699, 'Reußenweg', 19936),
(20700, 'Reuterstraße', 19939),
(20701, 'Rhönstraße', 19938),
(20702, 'Richard-Strauß-Straße', 19937),
(20703, 'Richard-Wagner-Straße', 19937),
(20704, 'Riedelspfad', 19936),
(20705, 'Riedstraße', 19941),
(20706, 'Riemenschneiderstraße ger. Nr.', 19943),
(20707, 'Riemenschneiderstraße ung. Nr.', 19935),
(20708, 'Rimparer Steig', 19938),
(20709, 'Rimparer Straße', 19938),
(20710, 'Ringstraße', 19936),
(20711, 'Rittergasse', 19935),
(20712, 'Ritterstiftstraße', 19941),
(20713, 'Robert-Bunsen-Straße', 19938),
(20714, 'Robert-Kirchhoff-Straße', 19941),
(20715, 'Robert-Koch-Straße', 19938),
(20716, 'Rochesterstraße', 403107),
(20717, 'Rochusgasse', 19936),
(404557, 'Roland-Frank-Straße', 19941),
(20718, 'Römer Straße', 403108),
(20719, 'Römische Klinge', 19945),
(20720, 'Röntgenring', 19935),
(20760, 'Rosa-Buchbinder-Straße', 19937),
(20721, 'Rosa-Hahn-Straße', 19945),
(20722, 'Rosengasse', 19935),
(20723, 'Rosenmühlweg', 19938),
(20724, 'Roßbergweg', 19944),
(20725, 'Rotenburstraße', 19940),
(20726, 'Rotenhanstraße', 19946),
(20727, 'Rothäckerweg', 19944),
(20728, 'Röthenweg', 19939),
(20729, 'Rothofstraße', 19936),
(20730, 'Rothweg', 19944),
(20731, 'Rotkäppchenweg', 19939),
(20732, 'Rotkreuzsteige', 19938),
(20733, 'Rotkreuzstraße', 19935),
(20734, 'Rotlöwengasse', 19935),
(20735, 'Rotscheibengasse', 19935),
(20736, 'Rottenbauerer Grund', 19940),
(20737, 'Rottendorfer Straße 1-15', 19935),
(20738, 'Rottendorfer Straße 15a-Ende', 19937),
(20739, 'Rübezahlweg', 19939),
(20740, 'Rückermainstraße', 19935),
(20741, 'Rückertstraße', 19943),
(20742, 'Rüdigerstraße', 19935),
(20743, 'Rudolf-Clausius-Straße', 19936),
(20744, 'Ruppertsgasse', 19939),
(506802, 'Ruth-Pfau-Straße', 19937),
(20745, 'Saalgasse', 19946),
(20746, 'Salamancastraße', 403107),
(20747, 'Salvatorstraße', 19937),
(20748, 'Sandäcker', 19941),
(20749, 'Sandbergerstraße', 19937),
(20750, 'Sandbergstraße', 19937),
(20751, 'Sanderglacisstraße', 19943),
(20752, 'Sanderheimrichsleitenweg', 19937),
(20753, 'Sanderring', 19935),
(20754, 'Sanderrothstraße', 19937),
(20755, 'Sanderstraße', 19935),
(20756, 'Sandgrubenweg', 19939),
(20757, 'Sandweg', 19938),
(20758, 'Sartoriusstraße', 19935),
(20759, 'Scanzonistraße', 19935),
(20761, 'Schafhofstraße', 19936),
(20762, 'Schalksbergweg', 19938),
(20763, 'Schanzstraße', 19937),
(20764, 'Scharnhorststraße', 19946),
(20765, 'Scharoldstraße', 19938),
(20766, 'Schattbergweg', 403107),
(20767, 'Scheffelstraße', 19943),
(20768, 'Schellingstraße', 19937),
(20769, 'Schenkenschloßweg', 19936),
(20770, 'Schenkhof', 19935),
(20771, 'Scherenbergstraße', 19946),
(20772, 'Schießhausstraße', 19943),
(20773, 'Schiestlstraße', 19938),
(20774, 'Schildhof', 19935),
(20775, 'Schildweg', 19939),
(20776, 'Schillerstraße', 19943),
(20777, 'Schlehenweg', 19941),
(20778, 'Schleifweg', 19940),
(20779, 'Schlesierstraße', 19942),
(20780, 'Schlörstraße', 19937),
(20781, 'Schloßgasse', 403103),
(20782, 'Schloßhecke', 19940),
(20783, 'Schmalzmarkt', 19935),
(20784, 'Schneewittchenweg', 19939),
(20785, 'Schollergasse', 19939),
(20786, 'Schöllhammerweg', 19944),
(20787, 'Schönbornstraße', 19935),
(20788, 'Schönleinstraße', 19935),
(20789, 'Schönthalstraße', 19935),
(20790, 'Schöpf', 19941),
(20791, 'Schorkstraße', 19946),
(20792, 'Schottenanger', 403103),
(20793, 'Schulstraße', 19940),
(20794, 'Schulzenstraße', 19940),
(20796, 'Schürerstraße', 19935),
(20797, 'Schustergasse', 19935),
(20798, 'Schüttgasse', 19935),
(20799, 'Schützensteige', 19941),
(20800, 'Schwabenstraße', 19942),
(20801, 'Schwanenhof', 19935),
(20802, 'Schweinfurter Straße 2-13', 19935),
(20803, 'Schweinfurter Straße 26-Ende', 19938),
(20804, 'Sebastianisteig', 19944),
(20805, 'Sebastian-Kneipp-Weg', 19944),
(20806, 'Sebastian-Merkle-Straße', 19937),
(20807, 'Sedanstraße', 19946),
(20808, 'Seegartenweg', 19939),
(20809, 'Seelbergstraße', 19935),
(20810, 'Seepfad', 19941),
(20811, 'Seeweg', 19946),
(20812, 'Seilerstraße', 19939),
(20813, 'Seinsheimstraße', 19937),
(20814, 'Semmelstraße', 19935),
(20815, 'Senefelder Straße', 19938),
(20816, 'Seuffertstraße', 19937),
(20817, 'Siebenbürgenstraße', 19945),
(20818, 'Sieboldstraße', 19943),
(20819, 'Siedlungsstraße', 19936),
(20820, 'Silcherstraße', 19937),
(20821, 'Siligmüllerstraße', 19935),
(20822, 'Simon-Blenk-Weg', 401083),
(20823, 'Simon-Breu-Straße', 19937),
(505738, 'Skyline-Hill-Straße', 19937),
(20824, 'Sodenstraße', 19937),
(20825, 'Sonnenhang', 19941),
(20826, 'Sonnenstraße', 19943),
(20827, 'Sonnenweg', 19936),
(20828, 'Sonnleite', 19941),
(20829, 'Sophienstraße', 19943),
(20830, 'Spartaweg', 403107),
(20831, 'Spechtweg', 19944),
(20832, 'Spessartstraße', 19946),
(20833, 'Spiegelstraße', 19935),
(20834, 'Spitalgasse', 403103),
(20835, 'Spitalweg', 19944),
(20836, 'Spittelbergweg', 19944),
(20837, 'Spitztannenweg', 403107),
(20844, 'Ständerbühlstraße', 19938),
(20845, 'Stauferstraße', 19941),
(20846, 'Stauffenbergstraße', 19940),
(20838, 'St.-Benedikt-Straße', 19935),
(20847, 'Stegenturmgasse', 19939),
(20848, 'Stegerwaldstraße', 19937),
(20849, 'Steidlestraße', 19937),
(20850, 'Steigerfurtweg', 19939),
(20851, 'Steigerwaldstraße', 19941),
(20852, 'Steigstraße', 19945),
(20853, 'Steigwaldweg', 403107),
(20854, 'Steinachstraße', 19946),
(20855, 'Steinbachtal', 19944),
(20856, 'Steinbruchweg', 19941),
(20857, 'Steinburgstraße', 19936),
(20858, 'Steinhäuserstraße', 19939),
(20859, 'Steinheilstraße', 19938),
(20860, 'Steinlein', 19945),
(20861, 'Steinstraße', 19935),
(20862, 'Stengerstraße', 19939),
(20863, 'Stephanstraße', 19935),
(20864, 'Sterenstraße', 19937),
(20865, 'Sterngasse', 19935),
(20866, 'Sterntalerweg', 19939),
(20867, 'Stettiner Straße', 19943),
(20868, 'Steubenstraße', 19937),
(20839, 'St.-Jakobus-Straße', 19945),
(20840, 'St.-Josef-Straße', 19936),
(20841, 'St.-Lioba-Straße', 401083),
(20869, 'Stockholmer Straße', 403107),
(20870, 'Stöhrstraße', 19937),
(20871, 'Straßburger Ring', 403107),
(20872, 'Straße zum Waldfriedhof', 19944),
(20873, 'Straubmühlweg', 506176),
(20842, 'St.-Rochus-Straße', 19945),
(20843, 'St.-Stephan-Straße', 19936),
(20874, 'Stürzpfad', 19939),
(20875, 'Stuttgarter Straße', 19939),
(20876, 'Sudetenstraße', 19942),
(20877, 'Südliche Hafenstraße', 19936),
(20878, 'Talavera', 19946),
(20879, 'Talweg', 401083),
(20880, 'Tannenweg', 19940),
(20881, 'Taschenäckerweg', 19939),
(20882, 'Taschenpfad', 19941),
(20883, 'Tellsteige', 403103),
(20884, 'Textorstraße', 19935),
(20885, 'Theaterstraße', 19935),
(20886, 'Thebenweg', 403107),
(20887, 'Theodor-Boveri-Weg', 19937),
(20888, 'Theodor-Heuss-Damm', 19943),
(20889, 'Theodor-Körner-Straße', 19943),
(20337, 'Theresia-Winterstein-Straße', 19937),
(20890, 'Theresienstraße', 19935),
(20891, 'Thüringerstraße', 19942),
(20892, 'Tiefe Gasse', 19939),
(20893, 'Tiepolostraße', 19935),
(20894, 'Tilsiter Straße', 19943),
(20895, 'Tokiostraße', 403107),
(20896, 'Toräckerweg', 19939),
(20897, 'Traubengasse', 19943),
(20898, 'Trautenauer Straße', 19937),
(20899, 'Trojaweg', 403107),
(20900, 'Tröltschstraße', 19935),
(20901, 'Tulpenstraße', 19940),
(20902, 'Turmgasse', 19935),
(20903, 'Uhlandstraße', 19943),
(20904, 'Ulmenstraße', 19940),
(20905, 'Ulmer Hof', 19935),
(20906, 'Ulrichstraße', 19937),
(20907, 'Unterdürrbacher Straße', 19936),
(20908, 'Untere Bockgasse', 19935),
(20909, 'Untere Goldbergstraße', 19945),
(20910, 'Untere Heerbergstraße', 19945),
(20911, 'Untere Hofgasse', 19945),
(20912, 'Untere Johannitergasse', 19935),
(20913, 'Unterer Adelbergweg', 19945),
(20914, 'Unterer Dallenbergweg', 19944),
(20915, 'Unterer Hublandweg', 19937),
(20916, 'Unterer Katzenbergweg', 19939),
(20917, 'Unterer Kaulweg', 19939),
(20918, 'Unterer Kirchbergweg', 19939),
(20919, 'Unterer Kirchplatz', 19940),
(20920, 'Unterer Kühlenberg', 19945),
(20921, 'Unterer Neubergweg', 19937),
(20922, 'Unterer Steinbergweg', 19936),
(20923, 'Unterer Torweinberg', 19940),
(20924, 'Unterer Wandweg', 19936),
(20925, 'Unterer Weg', 19939),
(20926, 'Urlaubstraße', 19938),
(20927, 'Ursulinergasse', 19935),
(20928, 'V.-A.-Fischer-Weg', 19944),
(20929, 'Valentin-Becker-Straße', 19935),
(20930, 'Veitshöchheimer Straße 1-5 ung./2-30 ger. Nr.', 19935),
(20931, 'Veitshöchheimer Straße 7-Ende ung./32-Ende ger. Nr.', 19936),
(20932, 'Versbacher Röthe', 19945),
(506464, 'Versbacher Straße 3-33 ung. Nr. / 4-58 ger. Nr.', 506176),
(506463, 'Versbacher Straße 39-99 ung.', 19942),
(20933, 'Versbacher Straße 100-Ende', 19945),
(20934, 'Versbacher Straße 3-33 ung. Nr.', 19938),
(20935, 'Versbacher Straße 39-99 ung./4-92 ger. Nr.', 19942),
(20936, 'Vierter Siedlungsweg', 19946),
(20937, 'Virchowstraße', 19943),
(20938, 'Vogelsangweg', 19941),
(20939, 'Vogelweiderweg', 19937),
(20940, 'Voglerstraße', 19937),
(20941, 'Von-Luxburg-Straße', 19937),
(20942, 'Von-Mieg-Straße', 19946),
(20943, 'Vorderer Johannishof', 19944),
(403117, 'Wacholderweg', 19940),
(20944, 'Wagnerplatz', 19938),
(20945, 'Wagnerstraße', 19938),
(20946, 'Waidmannsau', 19940),
(20947, 'Waidmannsteige', 19941),
(20948, 'Waldkugelweg', 19944),
(20949, 'Wallgasse', 19935),
(20950, 'Wallkrone', 19935),
(20951, 'Walter-Stier-Straße', 19945),
(20952, 'Walther-Nernst-Straße', 19936),
(20953, 'Waltherstraße', 19937),
(20954, 'Walther-von-der-Vogelweide-Straße', 19937),
(20955, 'Wandweg', 19936),
(20956, 'Warschauer Straße', 403107),
(20957, 'Weg an der Ziegelhütte', 19939),
(20958, 'Weg zum Sportplatz', 19941),
(20959, 'Weg zur Neuen Welt', 19939),
(20960, 'Weg zur Zeller Waldspitze', 19946),
(20961, 'Weidenstraße', 19940),
(20962, 'Weinbergweg', 19936),
(20963, 'Weingartenstraße', 19943),
(20964, 'Weißbrückengraben', 19939),
(20965, 'Weißdornweg', 19940),
(20966, 'Weißenburgstraße', 19946),
(20967, 'Weißer Bildweg', 19936),
(20968, 'Wellhöferweg', 19939),
(20969, 'Welzstraße', 19935),
(20970, 'Wendelweg', 19939),
(20971, 'Wenzelstraße', 19939),
(20972, 'Werkingstraße', 19939),
(20973, 'Werner-von-Siemens-Straße 1-27', 19938),
(20974, 'Werner-von-Siemens-Straße 28-Ende', 19941),
(20975, 'Wickenmayerstraße', 19938),
(20976, 'Wiener Ring', 403107),
(20977, 'Wiesenweg', 19939),
(20978, 'Wilhelm-Dahl-Straße', 19946),
(20979, 'Wilhelm-Schwinn-Platz', 19935),
(20980, 'Wilhelmstraße', 19935),
(20981, 'Wilhelm-Wien-Straße', 19936),
(20982, 'Winterhäuser Straße', 19939),
(20983, 'Winterhäuser Weg', 19940),
(20984, 'Winterleitenweg', 19944),
(20985, 'Wirsbergstraße', 19935),
(20986, 'Wittelsbacherplatz', 19937),
(20987, 'Wittelsbacherstraße', 19937),
(20988, 'Wölffelstraße', 19943),
(20989, 'Wolfhartsgasse', 19935),
(20990, 'Wolframstraße', 19935),
(20991, 'Wolfskeelstraße', 19940),
(20992, 'Wöllergasse', 19935),
(20993, 'Wörthstraße', 19946),
(20994, 'Wredestraße', 19946),
(403118, 'Würzburger Höhe', 19940),
(20996, 'Ysenburgstraße', 19946),
(20997, 'Zehntgasse', 19940),
(20998, 'Zehnthofstraße', 19936),
(21000, 'Zellerangen-Forst', 19946),
(20999, 'Zeller Straße', 403103),
(21001, 'Zeppelinstraße', 19937),
(21002, 'Ziegelaustraße', 19935),
(21003, 'Ziegelhütte', 19936),
(21004, 'Zindelgasse', 19939),
(21005, 'Zinkhof', 19935),
(21006, 'Zinklesweg', 19938),
(21007, 'Zobelweg', 19939),
(21008, 'Zülbsgasse', 19939),
(21009, 'Zum Himmelreich', 19940),
(21010, 'Zum Sportplatz', 19936),
(21011, 'Zum Storchenbrünnlein', 19940),
(21012, 'Zum Tännig', 19945),
(21013, 'Zu-Rhein-Straße', 19937),
(21014, 'Zürnstraße', 19937),
(403119, 'Zur Würzburger Mehle', 19940),
(21015, 'Zweierweg', 19937),
(21016, 'Zweite Felsengasse', 403103),
(21017, 'Zweiter Siedlungsweg', 19946),
(21018, 'Zwerchgraben', 19937),
(21019, 'Zwinger', 19935);


INSERT INTO garbage_type (id, name) VALUES
(1, 'Biomüll'),
(2, 'Gelbe Säcke'),
(3, 'Papier'),
(4, 'Restmüll'),
(5, 'Wertstoffmobil');


INSERT INTO state (id, name) VALUES
(1, 'Empty'),
(2, 'Middle'),
(3, 'Full'),
(4, 'Overfull');