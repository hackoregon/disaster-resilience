-- View: public."POI_view"

-- DROP VIEW public."POI_view";

CREATE OR REPLACE VIEW public."POI_view" AS 
 SELECT
    'BEECN'||basic_earthquake_emergency_communication_node_beecn_locations.ogc_fid as pk_id,
    basic_earthquake_emergency_communication_node_beecn_locations.ogc_fid,
    'BEECN'::text AS type,
    basic_earthquake_emergency_communication_node_beecn_locations.hub_name AS description_txt,
    basic_earthquake_emergency_communication_node_beecn_locations.site_name AS description2_txt,
    basic_earthquake_emergency_communication_node_beecn_locations.location AS address,
    'Portland'::character varying AS city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (st_dump(st_transform(basic_earthquake_emergency_communication_node_beecn_locations.wkb_geometry, 4326))).geom AS wkb_geometry
   FROM basic_earthquake_emergency_communication_node_beecn_locations
UNION
 SELECT
    'Fire Station'||fire_sta.ogc_fid as pk_id,
    fire_sta.ogc_fid,
    'Fire Station'::text AS type,
    fire_sta.station AS description_txt,
    fire_sta.district AS description2_txt,
    fire_sta.address,
    fire_sta.city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (st_dump(st_transform(fire_sta.wkb_geometry, 4326))).geom AS wkb_geometry
   FROM fire_sta
UNION
 SELECT
    'Hospital'||hospital.ogc_fid as pk_id,
   hospital.ogc_fid,
    'Hospital'::text AS type,
    hospital.name AS description_txt,
    ''::character varying AS description2_txt,
    hospital.address,
    hospital.city,
    'OR'::text AS state,
    ''::text AS zipcode,
    (st_dump(st_transform(hospital.wkb_geometry, 4326))).geom AS wkb_geometry
   FROM hospital
UNION
 SELECT
    'School'||schools.ogc_fid as pk_id,
    schools.ogc_fid,
    'School'::text AS type,
    schools.name AS description_txt,
    schools.level_name AS description2_txt,
    schools.address,
    schools.city,
    schools.state,
    schools.zipcode,
    (st_dump(st_transform(schools.wkb_geometry, 4326))).geom AS wkb_geometry
   FROM schools
UNION
	SELECT
		'COMMCTR'||ogc_fid as pk_id,
		ogc_fid,
		'COMMCTR' as type,
		name as description_txt, 
		owner as description2_txt,
		address||' '||address2 as address, 
		city, 
		state, 
		zipcode||' ' ||zip4 as zipcode,
		wkb_geometry
	FROM public.community_centers;


ALTER TABLE public."POI_view"
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public."POI_view" TO "disaster-resilience";
GRANT SELECT ON TABLE public."POI_view" TO "disaster-resilience-readonly";
