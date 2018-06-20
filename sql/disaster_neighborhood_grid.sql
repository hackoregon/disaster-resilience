-- Table: public.disaster_neighborhood_grid

-- DROP TABLE public.disaster_neighborhood_grid;

CREATE TABLE public.disaster_neighborhood_grid
(
  id integer NOT NULL,
  centroidx character varying(255),
  centroidy character varying(255),
  x_simple character varying(255),
  y_simple character varying(255),
  wkb_geometry geometry,
  pgv_site_count character varying(255),
  pgv_site_max character varying(255),
  pgv_site_mean character varying(255),
  pgv_site_min character varying(255),
  pgv_site_std character varying(255),
  pgd_landslide_dry_count character varying(255),
  pgd_landslide_dry_max character varying(255),
  pgd_landslide_dry_mean character varying(255),
  pgd_landslide_dry_min character varying(255),
  pgd_landslide_dry_std character varying(255),
  pgd_landslide_wet_count character varying(255),
  pgd_landslide_wet_max character varying(255),
  pgd_landslide_wet_mean character varying(255),
  pgd_landslide_wet_min character varying(255),
  pgd_landslide_wet_std character varying(255),
  pgd_liquefaction_wet_count character varying(255),
  pgd_liquefaction_wet_max character varying(255),
  pgd_liquefaction_wet_mean character varying(255),
  pgd_liquefaction_wet_min character varying(255),
  pgd_liquefaction_wet_std character varying(255),
  pgd_total_wet_mean character varying(255),
  pgv_site_min_mmi integer,
  pgv_site_max_mmi integer,
  pgv_site_mean_mmi integer,
  pgd_landslide_dry_min_di character varying(255),
  pgd_landslide_dry_max_di character varying(255),
  pgd_landslide_dry_mean_di character varying(255),
  pgd_landslide_wet_min_di character varying(255),
  pgd_landslide_wet_max_di character varying(255),
  pgd_landslide_wet_mean_di character varying(255),
  pgd_liquefaction_wet_min_di character varying(255),
  pgd_liquefaction_wet_max_di character varying(255),
  pgd_liquefaction_wet_mean_di character varying(255),
  pgd_total_wet_mean_di character varying(255),
  CONSTRAINT disaster_neighborhood_grid_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.disaster_neighborhood_grid
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public.disaster_neighborhood_grid TO "disaster-resilience";
GRANT SELECT ON TABLE public.disaster_neighborhood_grid TO "disaster-resilience-readonly";
