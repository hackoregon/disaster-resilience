
-- View: public.disaster_neighborhood_view

-- DROP VIEW public.disaster_neighborhood_view;

CREATE OR REPLACE VIEW public.disaster_neighborhood_view AS 
 SELECT 
    dn.id,
    dn.name,
    dn.wkb_geometry,
    dn.pgv_site_count,
    dn.pgv_site_max,
    dn.pgv_site_mean,
    dn.pgv_site_min,
    dn.pgv_site_std,
    dn.pgd_landslide_dry_count,
    dn.pgd_landslide_dry_max,
    dn.pgd_landslide_dry_mean,
    dn.pgd_landslide_dry_min,
    dn.pgd_landslide_dry_std,
    dn.pgd_landslide_wet_count,
    dn.pgd_landslide_wet_max,
    dn.pgd_landslide_wet_mean,
    dn.pgd_landslide_wet_min,
    dn.pgd_landslide_wet_std,
    dn.pgd_liquefaction_wet_count,
    dn.pgd_liquefaction_wet_max,
    dn.pgd_liquefaction_wet_mean,
    dn.pgd_liquefaction_wet_min,
    dn.pgd_liquefaction_wet_std,
    dn.pgd_total_wet_mean,
    dn.pgv_site_min_mmi,
    dn.pgv_site_max_mmi,
    dn.pgv_site_mean_mmi,
    dn.pgd_landslide_dry_min_di,
    dn.pgd_landslide_dry_max_di,
    dn.pgd_landslide_dry_mean_di,
    dn.pgd_landslide_wet_min_di,
    dn.pgd_landslide_wet_max_di,
    dn.pgd_landslide_wet_mean_di,
    dn.pgd_liquefaction_wet_min_di,
    dn.pgd_liquefaction_wet_max_di,
    dn.pgd_liquefaction_wet_mean_di,
    dn.pgd_total_wet_mean_di,
    mmin.id AS pgv_site_min_mmi_id,
    ((mmin.detail_txt::text || ' ('::text) || mmin.value_txt::text) || ')'::text AS pgv_site_min_mmi_txt,
    mmax.id AS pgv_site_max_mmi_id,
    ((mmax.detail_txt::text || ' ('::text) || mmax.value_txt::text) || ')'::text AS pgv_site_max_mmi_txt,
    mmean.id AS pgv_site_mean_mmi_id,
    ((mmean.detail_txt::text || ' ('::text) || mmean.value_txt::text) || ')'::text AS pgv_site_mean_mmi_txt
   FROM disaster_neighborhoods dn
     JOIN mercalli mmin ON mmin.id = dn.pgv_site_min_mmi
     JOIN mercalli mmax ON mmax.id = dn.pgv_site_max_mmi
     JOIN mercalli mmean ON mmean.id = dn.pgv_site_mean_mmi
 union
 SELECT
    dn.id,
    'Grid' as name,
    dn.wkb_geometry,
    dn.pgv_site_count,
    dn.pgv_site_max,
    dn.pgv_site_mean,
    dn.pgv_site_min,
    dn.pgv_site_std,
    dn.pgd_landslide_dry_count,
    dn.pgd_landslide_dry_max,
    dn.pgd_landslide_dry_mean,
    dn.pgd_landslide_dry_min,
    dn.pgd_landslide_dry_std,
    dn.pgd_landslide_wet_count,
    dn.pgd_landslide_wet_max,
    dn.pgd_landslide_wet_mean,
    dn.pgd_landslide_wet_min,
    dn.pgd_landslide_wet_std,
    dn.pgd_liquefaction_wet_count,
    dn.pgd_liquefaction_wet_max,
    dn.pgd_liquefaction_wet_mean,
    dn.pgd_liquefaction_wet_min,
    dn.pgd_liquefaction_wet_std,
    dn.pgd_total_wet_mean,
    dn.pgv_site_min_mmi,
    dn.pgv_site_max_mmi,
    dn.pgv_site_mean_mmi,
    dn.pgd_landslide_dry_min_di,
    dn.pgd_landslide_dry_max_di,
    dn.pgd_landslide_dry_mean_di,
    dn.pgd_landslide_wet_min_di,
    dn.pgd_landslide_wet_max_di,
    dn.pgd_landslide_wet_mean_di,
    dn.pgd_liquefaction_wet_min_di,
    dn.pgd_liquefaction_wet_max_di,
    dn.pgd_liquefaction_wet_mean_di,
    dn.pgd_total_wet_mean_di,
    mmin.id AS pgv_site_min_mmi_id,
    ((mmin.detail_txt::text || ' ('::text) || mmin.value_txt::text) || ')'::text AS pgv_site_min_mmi_txt,
    mmax.id AS pgv_site_max_mmi_id,
    ((mmax.detail_txt::text || ' ('::text) || mmax.value_txt::text) || ')'::text AS pgv_site_max_mmi_txt,
    mmean.id AS pgv_site_mean_mmi_id,
    ((mmean.detail_txt::text || ' ('::text) || mmean.value_txt::text) || ')'::text AS pgv_site_mean_mmi_txt
   FROM disaster_neighborhood_grid dn
     JOIN mercalli mmin ON mmin.id = dn.pgv_site_min_mmi
     JOIN mercalli mmax ON mmax.id = dn.pgv_site_max_mmi
     JOIN mercalli mmean ON mmean.id = dn.pgv_site_mean_mmi;

ALTER TABLE public."disaster_neighborhood_view"
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public."disaster_neighborhood_view" TO "disaster-resilience";
GRANT SELECT ON TABLE public."disaster_neighborhood_view" TO "disaster-resilience-readonly";
