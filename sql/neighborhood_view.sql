-- View: public.neighborhood_view

-- DROP VIEW public.neighborhood_view;

CREATE OR REPLACE VIEW public.neighborhood_view AS 
 SELECT nr.ogc_fid,
    nr.objectid,
    nr.name,
    nr.commplan,
    nr.shared,
    nr.coalit,
    nr.horz_vert,
    nr.maplabel,
    nr.id,
    nr.shape_leng,
    nr.shape_area AS region_shape_area,
    nr.wkb_geometry AS region_wkb_geometry,
    nu.shape_length,
    nu.shape_area AS unit_shape_area,
    nu.nuid,
    nu.county,
    nu.acres,
    nu.bldgcount,
    nu.bldgsqft,
    nu.bldgcost,
    nu.bldgweight,
    nu.contentcost,
    nu.permresidents,
    nu.dayoccupants,
    nu.nightoccupants,
    nu.wkb_geometry AS unit_wkb_geometry
   FROM neighborhood_units nu
     JOIN neighborhoods_regions nr ON nr.id = nu.nuid::numeric;

ALTER TABLE public.neighborhood_view
  OWNER TO postgres;
