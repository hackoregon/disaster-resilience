-- table: public.disaster_neighborhoods

drop table public.disaster_neighborhoods;

create table public.disaster_neighborhoods(
	id integer primary key,
	fid integer,
	name varchar(255),
	area varchar(255),
	sqmile varchar(255),
	area_recal varchar(255),
	perim varchar(255),
	isop varchar(255),
	wkb_geometry geometry,
	pgv_site_count varchar(255),
	pgv_site_max varchar(255),
	pgv_site_mean varchar(255),
	pgv_site_min varchar(255),
	pgv_site_std varchar(255),
	pgd_landslide_dry_count varchar(255),
	pgd_landslide_dry_max varchar(255),
	pgd_landslide_dry_mean varchar(255),
	pgd_landslide_dry_min varchar(255),
	pgd_landslide_dry_std varchar(255),
	pgd_landslide_wet_count varchar(255),
	pgd_landslide_wet_max varchar(255),
	pgd_landslide_wet_mean varchar(255),
	pgd_landslide_wet_min varchar(255),
	pgd_landslide_wet_std varchar(255),
	pgd_liquefaction_wet_count varchar(255),
	pgd_liquefaction_wet_max varchar(255),
	pgd_liquefaction_wet_mean varchar(255),
	pgd_liquefaction_wet_min varchar(255),
	pgd_liquefaction_wet_std varchar(255),
	pgv_site_min_mmi varchar(255),
	pgv_site_max_mmi varchar(255),
	pgv_site_mean_mmi varchar(255),
	pgd_landslide_dry_min_di varchar(255),
	pgd_landslide_dry_max_di varchar(255),
	pgd_landslide_dry_mean_di varchar(255),
	pgd_landslide_wet_min_di varchar(255),
	pgd_landslide_wet_max_di varchar(255),
	pgd_landslide_wet_mean_di varchar(255),
	pgd_liquefaction_wet_min_di varchar(255),
	pgd_liquefaction_wet_max_di varchar(255),
	pgd_liquefaction_wet_mean_di varchar(255)
);

alter table public.disaster_neighborhoods
  owner to "disaster-resilience";
