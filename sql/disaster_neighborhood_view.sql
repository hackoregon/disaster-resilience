
-- View: public.disaster_neighborhood_view

-- DROP VIEW public.disaster_neighborhood_view;

CREATE OR REPLACE VIEW public.disaster_neighborhood_view AS 
SELECT
	dn.id,
	name,
	wkb_geometry,
	pgv_site_count,
	pgv_site_max,
	pgv_site_mean,
	pgv_site_min,
	pgv_site_std,
	pgd_landslide_dry_count,
	pgd_landslide_dry_max,
	pgd_landslide_dry_mean,
	pgd_landslide_dry_min,
	pgd_landslide_dry_std,
	pgd_landslide_wet_count,
	pgd_landslide_wet_max,
	pgd_landslide_wet_mean,
	pgd_landslide_wet_min,
	pgd_landslide_wet_std,
	pgd_liquefaction_wet_count,
	pgd_liquefaction_wet_max,
	pgd_liquefaction_wet_mean,
	pgd_liquefaction_wet_min,
	pgd_liquefaction_wet_std,
	pgd_total_wet_mean,
	pgv_site_min_mmi,
	pgv_site_max_mmi,
	pgv_site_mean_mmi,
	pgd_landslide_dry_min_di,
	pgd_landslide_dry_max_di,
	pgd_landslide_dry_mean_di,
	pgd_landslide_wet_min_di,
	pgd_landslide_wet_max_di,
	pgd_landslide_wet_mean_di,
	pgd_liquefaction_wet_min_di,
	pgd_liquefaction_wet_max_di,
	pgd_liquefaction_wet_mean_di,
	pgd_total_wet_mean_di,
	mmin.id as pgv_site_min_mmi_id,
	mmin.detail_txt||' ('||mmin.value_txt||')' as pgv_site_min_mmi_txt,
	mmax.id pgv_site_max_mmi_id,
	mmax.detail_txt||' ('||mmax.value_txt||')' as pgv_site_max_mmi_txt,
	mmean.id pgv_site_mean_mmi_id,
	mmean.detail_txt||' ('||mmean.value_txt||')' as pgv_site_mean_mmi_txt
FROM public.disaster_neighborhoods dn
	join public.mercalli mmin on mmin.id = pgv_site_min_mmi
	join public.mercalli mmax on mmax.id = pgv_site_max_mmi
	join public.mercalli mmean on mmean.id = pgv_site_mean_mmi;

ALTER TABLE public."disaster_neighborhood_view"
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public."disaster_neighborhood_view" TO "disaster-resilience";
GRANT SELECT ON TABLE public."disaster_neighborhood_view" TO "disaster-resilience-readonly";
