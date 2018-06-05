-- View: public.POI_view

-- DROP VIEW public.POI_view;

CREATE OR REPLACE VIEW public.POI_view AS
SELECT 
  ogc_fid,
  'BEECN' as type, 
  hub_name as description_txt,
  site_name as description2_txt,
  location as address, 
  'Portland' as city, 
  'OR' as state, 
  '' as zipcode, 
  wkb_geometry
FROM public.basic_earthquake_emergency_communication_node_beecn_locations
union
SELECT
 ogc_fid, 
 'Fire Station' as type, 
 station as description_txt,
 district as description2_txt, 
 address,
  city, 
  'OR' as state, 
  '' as zipcode, 
 wkb_geometry
FROM public.fire_sta
union
SELECT
  ogc_fid, 
 'Hospital' as type, 
  name as description_txt, 
  '' as description2_txt,
  address, 
  city, 
  'OR' as state, 
  '' as zipcode, 
  wkb_geometry
FROM public.hospital
union
SELECT 
  ogc_fid, 
 'School' as type, 
  name as description_txt, 
  level_name as description2_txt, 
  address,
  city, 
  state, 
  zipcode, 
  wkb_geometry
FROM public.schools;

ALTER TABLE public.POI_view
  OWNER TO "disaster-resilience";
