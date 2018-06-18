-- View: public."POI_view"

-- DROP VIEW public."POI_view";

CREATE OR REPLACE VIEW public."POI_view" AS 
 SELECT
    'BEECN'::text || basic_earthquake_emergency_communication_node_beecn_locations.ogc_fid AS pk_id,
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
    'Fire Station'::text || fire_sta.ogc_fid AS pk_id,
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
    'Hospital'::text || hospital.ogc_fid AS pk_id,
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
    'School'::text || schools.ogc_fid AS pk_id,
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
   'COMMCTR'::text || community_centers.ogc_fid AS pk_id,
    community_centers.ogc_fid,
    'COMMCTR'::text AS type,
    community_centers.name AS description_txt,
    community_centers.owner AS description2_txt,
    (community_centers.address::text || ' '::text) || community_centers.address2::text AS address,
    community_centers.city,
    community_centers.state,
    (community_centers.zipcode::text || ' '::text) || community_centers.zip4::text AS zipcode,
    (st_dump(st_transform(community_centers.wkb_geometry, 4326))).geom AS wkb_geometry
   FROM community_centers
UNION
 SELECT 
	'NET'::text || row_number() OVER () as pk_id, 
	row_number() OVER () AS ogc_fid,
	'NET'::text as type,
	nets.description_txt,
	nets.location_txt as description2_txt,
	nets.location_dd_val as address,
	'' as city,
	'OR' as "state",
	'' as zipcode,
	ST_SetSRID(
	  st_makepoint(
	    split_part(nets.location_dd_val::text, ','::text, 2)::double precision, 
	    split_part(nets.location_dd_val::text, ','::text, 1)::double precision
	   ),
	  4326
	) AS wkb_geometry
  FROM nets;

ALTER TABLE public."POI_view"
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public."POI_view" TO "disaster-resilience";
GRANT SELECT ON TABLE public."POI_view" TO "disaster-resilience-readonly";
