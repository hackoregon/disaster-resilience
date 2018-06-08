-- View: public."POI_view"

-- DROP VIEW public."POI_view";

CREATE OR REPLACE VIEW public."POI_view" AS 
 SELECT basic_earthquake_emergency_communication_node_beecn_locations.ogc_fid,
    'BEECN'::text AS type,
    basic_earthquake_emergency_communication_node_beecn_locations.hub_name AS description_txt,
    basic_earthquake_emergency_communication_node_beecn_locations.site_name AS description2_txt,
    basic_earthquake_emergency_communication_node_beecn_locations.location AS address,
    'Portland'::character varying AS city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (ST_Dump(ST_Transform (basic_earthquake_emergency_communication_node_beecn_locations.wkb_geometry, 4326))).geom as wkb_geometry
--    basic_earthquake_emergency_communication_node_beecn_locations.wkb_geometry
   FROM basic_earthquake_emergency_communication_node_beecn_locations
UNION
 SELECT fire_sta.ogc_fid,
    'Fire Station'::text AS type,
    fire_sta.station AS description_txt,
    fire_sta.district AS description2_txt,
    fire_sta.address,
    fire_sta.city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (ST_Dump(ST_Transform (fire_sta.wkb_geometry, 4326))).geom as wkb_geometry
--    fire_sta.wkb_geometry
   FROM fire_sta
UNION
 SELECT hospital.ogc_fid,
    'Hospital'::text AS type,
    hospital.name AS description_txt,
    ''::character varying AS description2_txt,
    hospital.address,
    hospital.city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (ST_Dump(ST_Transform (hospital.wkb_geometry, 4326))).geom as wkb_geometry
--     hospital.wkb_geometry
   FROM hospital
UNION
 SELECT schools.ogc_fid,
    'School'::text AS type,
    schools.name AS description_txt,
    schools.level_name AS description2_txt,
    schools.address,
    schools.city,
    schools.state,
    schools.zipcode,
    (ST_Dump(ST_Transform (wkb_geometry, 4326))).geom as wkb_geometry
--    schools.wkb_geometry
   FROM schools;

ALTER TABLE public."POI_view"
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public."POI_view" TO "disaster-resilience";
GRANT SELECT ON TABLE public."POI_view" TO "disaster-resilience-readonly";
