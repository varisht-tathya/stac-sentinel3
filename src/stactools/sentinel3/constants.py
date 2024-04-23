import pystac
from pystac import ProviderRole
from pystac.extensions.eo import Band
from pystac.link import Link

INSPIRE_METADATA_ASSET_KEY = "inspire-metadata"
SAFE_MANIFEST_ASSET_KEY = "safe-manifest"
PRODUCT_METADATA_ASSET_KEY = "product-metadata"

MANIFEST_FILENAME = "xfdumanifest.xml"

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/"
    + "247904/690755/Sentinel_Data_Legal_Notice",
)

SENTINEL_CONSTELLATION = "Sentinel-3"

SENTINEL_PROVIDER = pystac.Provider(
    name="ESA",
    roles=[
        ProviderRole.PRODUCER,
        ProviderRole.PROCESSOR,
        ProviderRole.LICENSOR,
    ],
    url="https://earth.esa.int/web/guest/home",
)

SENTINEL_SLSTR_BANDS = {
    "S03": Band.create(
        name="S3",
        description="Band 3 - NDVI, cloud flagging, pixel co-registration",
        center_wavelength=868,
        full_width_half_max=20.6,
    ),
    "S06": Band.create(
        name="S6",
        description="Band 6 - Vegetation state and cloud clearing",
        center_wavelength=2255.7,
        full_width_half_max=50.15,
    ),
    "flags": Band.create(
        name="flags",
        description="Flags for clouds",
        center_wavelength=0,
        full_width_half_max=0,
    ),
    "geodetic": Band.create(
        name="geodetic",
        description="Band for georeferencing",
        center_wavelength=0,
        full_width_half_max=0,
    ),
}

SENTINEL_OLCI_BANDS = {
    "Oa03": Band.create(
        name="Oa03",
        description="Band 3 - Chlorophyll absorption "
        "maximum, biogeochemistry, vegetation",
        center_wavelength=442.5,
        full_width_half_max=10,
    ),
    "Oa06": Band.create(
        name="Oa06",
        description="Band 6 - Chlorophyll reference (minimum)",
        center_wavelength=560,
        full_width_half_max=10,
    ),
    "Oa08": Band.create(
        name="Oa08",
        description="Band 8 - 2nd Chlorophyll absorption "
        "maximum, sediment, yellow substance / vegetation",
        center_wavelength=665,
        full_width_half_max=10,
    ),
    "instrumentData": Band.create(
        name="instrumentDataAnnotation",
        description="Instrument Data",
        center_wavelength=1020,
        full_width_half_max=40,
    ),
    "tieMeteo": Band.create(
        name="tieMeteoAnnotation",
        description="Tie-Point Meteo Annotations",
        center_wavelength=1020,
        full_width_half_max=40,
    ),
    "tieGeometries": Band.create(
        name="tieGeometries",
        description="Tie-Point Geometries Annotations",
        center_wavelength=1020,
        full_width_half_max=40,
    ),
    "geoCoordinatesData": Band.create(
        name="tieGeoCoordinatesAnnotation",
        description="Tie-Point Geo Coordinate Annotations",
        center_wavelength=1020,
        full_width_half_max=40,
    ),
}

SENTINEL_SRAL_BANDS = {
    "C": Band.create(
        name="C",
        description="Band C - Ionospheric correction",
        center_wavelength=5409999872.000000,  # central frequency in Hz
        full_width_half_max=290000000.000000,  # bandwidth in Hz
    ),
    "Ku": Band.create(
        name="Ku",
        description="Band Ku - Range measurements",
        center_wavelength=13575000064.000000,  # central frequency in Hz
        full_width_half_max=320000000.000000,  # bandwidth in Hz
    ),
}

SENTINEL_SYNERGY_BANDS = {
    "SYN01": Band.create(
        name="SYN01",
        description="OLCI channel Oa01",
        center_wavelength=400,
        full_width_half_max=15,
    ),
    "SYN02": Band.create(
        name="SYN02",
        description="OLCI channel Oa02",
        center_wavelength=412.5,
        full_width_half_max=10,
    ),
    "SYN03": Band.create(
        name="SYN03",
        description="OLCI channel Oa03",
        center_wavelength=442.5,
        full_width_half_max=10,
    ),
    "SYN04": Band.create(
        name="SYN04",
        description="OLCI channel Oa04",
        center_wavelength=490,
        full_width_half_max=10,
    ),
    "SYN05": Band.create(
        name="SYN05",
        description="OLCI channel Oa05",
        center_wavelength=510,
        full_width_half_max=10,
    ),
    "SYN06": Band.create(
        name="SYN06",
        description="OLCI channel Oa06",
        center_wavelength=560,
        full_width_half_max=10,
    ),
    "SYN07": Band.create(
        name="SYN07",
        description="OLCI channel Oa07",
        center_wavelength=620,
        full_width_half_max=10,
    ),
    "SYN08": Band.create(
        name="SYN08",
        description="OLCI channel Oa08",
        center_wavelength=665,
        full_width_half_max=10,
    ),
    "SYN09": Band.create(
        name="SYN09",
        description="OLCI channel Oa09",
        center_wavelength=673.75,
        full_width_half_max=7.5,
    ),
    "SYN10": Band.create(
        name="SYN10",
        description="OLCI channel Oa10",
        center_wavelength=681.25,
        full_width_half_max=7.5,
    ),
    "SYN11": Band.create(
        name="SYN11",
        description="OLCI channel Oa11",
        center_wavelength=708.75,
        full_width_half_max=10,
    ),
    "SYN12": Band.create(
        name="SYN12",
        description="OLCI channel Oa12",
        center_wavelength=753.75,
        full_width_half_max=7.5,
    ),
    "SYN13": Band.create(
        name="SYN13",
        description="OLCI channel Oa16",
        center_wavelength=778.5,
        full_width_half_max=15,
    ),
    "SYN14": Band.create(
        name="SYN14",
        description="OLCI channel Oa17",
        center_wavelength=865,
        full_width_half_max=20,
    ),
    "SYN15": Band.create(
        name="SYN15",
        description="OLCI channel Oa18",
        center_wavelength=885,
        full_width_half_max=10,
    ),
    "SYN16": Band.create(
        name="SYN16",
        description="OLCI channel Oa21",
        center_wavelength=1020,
        full_width_half_max=40,
    ),
    "SYN17": Band.create(
        name="SYN17",
        description="SLSTR nadir channel S1",
        center_wavelength=555,
        full_width_half_max=20,
    ),
    "SYN18": Band.create(
        name="SYN18",
        description="SLSTR nadir channel S2",
        center_wavelength=659,
        full_width_half_max=20,
    ),
    "SYN19": Band.create(
        name="SYN19",
        description="SLSTR nadir channel S3",
        center_wavelength=865,
        full_width_half_max=20,
    ),
    "SYN20": Band.create(
        name="SYN20",
        description="SLSTR nadir channel S5",
        center_wavelength=1610,
        full_width_half_max=60,
    ),
    "SYN21": Band.create(
        name="SYN21",
        description="SLSTR nadir channel S6",
        center_wavelength=2250,
        full_width_half_max=50,
    ),
    "SYN22": Band.create(
        name="SYN22",
        description="SLSTR oblique channel S1",
        center_wavelength=555,
        full_width_half_max=20,
    ),
    "SYN23": Band.create(
        name="SYN23",
        description="SLSTR oblique channel S2",
        center_wavelength=659,
        full_width_half_max=20,
    ),
    "SYN24": Band.create(
        name="SYN24",
        description="SLSTR oblique channel S3",
        center_wavelength=865,
        full_width_half_max=20,
    ),
    "SYN25": Band.create(
        name="SYN25",
        description="SLSTR oblique channel S5",
        center_wavelength=1610,
        full_width_half_max=60,
    ),
    "SYN26": Band.create(
        name="SYN26",
        description="SLSTR oblique channel S6",
        center_wavelength=2250,
        full_width_half_max=50,
    ),
    "SYN_440": Band.create(
        name="SYN_440",
        description="OLCI channel Oa03",
        center_wavelength=442.5,
        full_width_half_max=10,
    ),
    "SYN_550": Band.create(
        name="SYN_550",
        description="SLSTR nadir and oblique channel S1",
        center_wavelength=550,
        full_width_half_max=20,
    ),
    "SYN_670": Band.create(
        name="SYN_670",
        description="SLSTR nadir and oblique channel S2",
        center_wavelength=659,
        full_width_half_max=20,
    ),
    "SYN_865": Band.create(
        name="SYN_865",
        description="OLCI channel Oa17, SLSTR nadir and oblique channel S2",
        center_wavelength=865,
        full_width_half_max=20,
    ),
    "SYN_1600": Band.create(
        name="SYN_1600",
        description="SLSTR nadir and oblique channel S5",
        center_wavelength=1610,
        full_width_half_max=60,
    ),
    "SYN_2250": Band.create(
        name="SYN_2250",
        description="SLSTR nadir and oblique channel S6",
        center_wavelength=2250,
        full_width_half_max=50,
    ),
    "B0": Band.create(
        name="B0",
        description="OLCI channels Oa02, Oa03",
        center_wavelength=450,
        full_width_half_max=20,
    ),
    "B2": Band.create(
        name="B2",
        description="OLCI channels Oa06, Oa07, Oa08, Oa09, Oa10",
        center_wavelength=645,
        full_width_half_max=35,
    ),
    "B3": Band.create(
        name="B3",
        description="OLCI channels Oa16, Oa17, Oa18, Oa21",
        center_wavelength=835,
        full_width_half_max=55,
    ),
    "MIR": Band.create(
        name="MIR",
        description="SLSTR nadir and oblique channels S5, S6",
        center_wavelength=1665,
        full_width_half_max=85,
    ),
}

OLCI_BANDS_TO_RESOLUTIONS = {
    "Oa01": [
        300,
    ],
    "Oa02": [
        300,
    ],
    "Oa03": [
        300,
    ],
    "Oa04": [
        300,
    ],
    "Oa05": [
        300,
    ],
    "Oa06": [
        300,
    ],
    "Oa07": [
        300,
    ],
    "Oa08": [
        300,
    ],
    "Oa09": [
        300,
    ],
    "Oa10": [
        300,
    ],
    "Oa11": [
        300,
    ],
    "Oa12": [
        300,
    ],
    "Oa13": [
        300,
    ],
    "Oa14": [
        300,
    ],
    "Oa15": [
        300,
    ],
    "Oa16": [
        300,
    ],
    "Oa17": [
        300,
    ],
    "Oa18": [
        300,
    ],
    "Oa19": [
        300,
    ],
    "Oa20": [
        300,
    ],
    "Oa21": [
        300,
    ],
}

SLSTR_BANDS_TO_RESOLUTIONS = {
    "S01": [
        500,
    ],
    "S02": [
        500,
    ],
    "S03": [
        500,
    ],
    "S04": [
        500,
    ],
    "S05": [
        500,
    ],
    "S06": [
        500,
    ],
    "S07": [
        1000,
    ],
    "S08": [
        1000,
    ],
    "S09": [
        1000,
    ],
    "S10": [
        1000,
    ],
    "S11": [
        1000,
    ],
    'flags':[
        500,
    ],
    "geodetic": [
        500,
    ],
}

SYNERGY_SYN_ASSET_KEYS = [
    "Syn_Oa01_reflectance_Data",
    "Syn_Oa02_reflectance_Data",
    "Syn_Oa03_reflectance_Data",
    "Syn_Oa04_reflectance_Data",
    "Syn_Oa05_reflectance_Data",
    "Syn_Oa06_reflectance_Data",
    "Syn_Oa07_reflectance_Data",
    "Syn_Oa08_reflectance_Data",
    "Syn_Oa09_reflectance_Data",
    "Syn_Oa10_reflectance_Data",
    "Syn_Oa11_reflectance_Data",
    "Syn_Oa12_reflectance_Data",
    "Syn_Oa16_reflectance_Data",
    "Syn_Oa17_reflectance_Data",
    "Syn_Oa18_reflectance_Data",
    "Syn_Oa21_reflectance_Data",
    "Syn_S1N_reflectance_Data",
    "Syn_S2N_reflectance_Data",
    "Syn_S3N_reflectance_Data",
    "Syn_S5N_reflectance_Data",
    "Syn_S6N_reflectance_Data",
    "Syn_S1O_reflectance_Data",
    "Syn_S2O_reflectance_Data",
    "Syn_S3O_reflectance_Data",
    "Syn_S5O_reflectance_Data",
    "Syn_S6O_reflectance_Data",
    "Syn_ATO550_Data",
    "Syn_Angstrom_exp550_Data",
    "Syn_SDR_removed_pixels_Data",
    "Syn_AMIN_Data",
    "Syn_flags_Data",
    "geolocation_Data",
    "time_Data",
    "annotations_removed_pixels_Data",
    "tiepoints_olci_Data",
    "tiepoints_slstr_n_Data",
    "tiepoints_slstr_o_Data",
    "tiepoints_meteo_Data",
]

SYNERGY_V10_VG1_ASSET_KEYS = [
    "b0Data",
    "b2Data",
    "b3Data",
    "mirData",
    "ndviData",
    "vaaData",
    "vzaData",
    "saaData",
    "szaData",
    "agData",
    "ogData",
    "wvgData",
    "tgData",
    "smData",
]

SYNERGY_VGP_ASSET_KEYS = [
    "b0Data",
    "b2Data",
    "b3Data",
    "mirData",
    "vaaData",
    "vzaData",
    "saaData",
    "szaData",
    "agData",
    "ogData",
    "wvgData",
    "smData",
]

OLCI_L1_ASSET_KEYS = [
    "Oa03_radianceData",
    "Oa06_radianceData",
    "Oa08_radianceData",
    "instrumentDataData",
    "tieMeteoData",
    "tieGeometriesData",
    "geoCoordinatesData",
]

OLCI_L2_LAND_ASSET_KEYS = [
    "ogviData",
    "otciData",
    "iwvData",
    "rcOgviData",
    "lqsfData",
    "timeCoordinatesData",
    "geoCoordinatesData",
    "tieGeoCoordinatesData",
    "tieGeometriesData",
    "tieMeteoData",
    "instrumentDataData",
]

OLCI_L2_LAND_ASSET_KEYS_RENAMED = [
    "gifaparData",
    "otciData",
    "iwvData",
    "rcGifaparData",
    "lqsfData",
    "timeCoordinatesData",
    "geoCoordinatesData",
    "tieGeoCoordinatesData",
    "tieGeometriesData",
    "tieMeteoData",
    "instrumentDataData",
]

OLCI_L2_WATER_ASSET_KEYS = [
    "Oa01_reflectanceData",
    "Oa02_reflectanceData",
    "Oa03_reflectanceData",
    "Oa04_reflectanceData",
    "Oa05_reflectanceData",
    "Oa06_reflectanceData",
    "Oa07_reflectanceData",
    "Oa08_reflectanceData",
    "Oa09_reflectanceData",
    "Oa10_reflectanceData",
    "Oa11_reflectanceData",
    "Oa12_reflectanceData",
    "Oa16_reflectanceData",
    "Oa17_reflectanceData",
    "Oa18_reflectanceData",
    "Oa21_reflectanceData",
    "chlNnData",
    "chlOc4meData",
    "iopNnData",
    "iwvData",
    "parData",
    "trspData",
    "tsmNnData",
    "wAerData",
    "geoCoordinatesData",
    "instrumentDataData",
    "tieGeoCoordinatesData",
    "tieGeometriesData",
    "tieMeteoData",
    "timeCoordinatesData",
    "wqsfData",
]

SLSTR_L1_ASSET_KEYS = [
    "SLSTR_S3_RAD_AN_Data",
    "SLSTR_S6_RAD_AN_Data",
    "SLSTR_GEODETIC_AN_Data",
    "SLSTR_FLAGS_AN_Data",
]

SLSTR_L2_FRP_KEYS = [
    "FRP_IN_Data",
    "SLSTR_CARTESIAN_FN_Data",
    "SLSTR_CARTESIAN_IN_Data",
    "SLSTR_CARTESIAN_TX_Data",
    "SLSTR_FLAGS_FN_Data",
    "SLSTR_FLAGS_IN_Data",
    "SLSTR_GEODETIC_FN_Data",
    "SLSTR_GEODETIC_IN_Data",
    "SLSTR_GEODETIC_TX_Data",
    "SLSTR_GEOMETRY_TN_Data",
    "SLSTR_INDICES_FN_Data",
    "SLSTR_INDICES_IN_Data",
    "SLSTR_MET_TX_Data",
    "SLSTR_TIME_IN_Data",
]

SLSTR_L2_LST_KEYS = [
    "LST_IN_Data",
    "LST_ANCILLARY_DS_Data",
    "SLSTR_FLAGS_IN_Data",
    "SLSTR_INDICES_IN_Data",
    "SLSTR_TIME_IN_Data",
    "SLSTR_GEODETIC_IN_Data",
    "SLSTR_CARTESIAN_IN_Data",
    "SLSTR_GEOMETRY_TN_Data",
    "SLSTR_GEODETIC_TX_Data",
    "SLSTR_CARTESIAN_TX_Data",
    "SLSTR_MET_TX_Data",
]

SRAL_L2_LAN_WAT_KEYS = [
    "standardMeasurementData",
    "enhancedMeasurementData",
    "reducedMeasurementData",
]

SYNERGY_L2_A550_T550_BANDS = [
    "S01",
    "S02",
    "S03",
    "S05",
    "S06",
    "Oa01",
    "Oa02",
    "Oa03",
    "Oa04",
    "Oa05",
    "Oa06",
    "Oa07",
    "Oa08",
    "Oa09",
    "Oa10",
    "Oa11",
    "Oa12",
    "Oa16",
    "Oa17",
    "Oa18",
    "Oa21",
]

SYNERGY_L2_SDR_BANDS = [
    "S01",
    "S02",
    "S03",
    "S04",
    "S06",
    "Oa01",
    "Oa02",
    "Oa03",
    "Oa04",
    "Oa05",
    "Oa06",
    "Oa07",
    "Oa08",
    "Oa09",
    "Oa10",
    "Oa11",
    "Oa12",
    "Oa13",
    "Oa16",
    "Oa17",
    "Oa18",
    "Oa19",
    "Oa21",
]

SENTINEL_OLCI_SLSTR_BANDS = {**SENTINEL_SLSTR_BANDS, **SENTINEL_OLCI_BANDS}

"""Mapping for any stac Asset keys which don't follow the default kebab-case rules.
This maps the resulting string in sen3_to_kebab, to the specially crafted version."""
SPECIAL_ASSET_KEYS = {"eopmetadata": "eop-metadata"}
