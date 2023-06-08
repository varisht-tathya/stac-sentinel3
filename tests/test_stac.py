from pathlib import Path

import pytest

from stactools.sentinel3 import stac
from stactools.sentinel3.constants import (
    OLCI_L1_ASSET_KEYS,
    OLCI_L2_LAND_ASSET_KEYS,
    OLCI_L2_LAND_ASSET_KEYS_RENAMED,
    OLCI_L2_WATER_ASSET_KEYS,
    SLSTR_L1_ASSET_KEYS,
    SLSTR_L2_FRP_KEYS,
    SLSTR_L2_LST_KEYS,
    SRAL_L2_LAN_WAT_KEYS,
    SYNERGY_SYN_ASSET_KEYS,
    SYNERGY_V10_VG1_ASSET_KEYS,
    SYNERGY_VGP_ASSET_KEYS,
)

ASSET_KEY_LISTS = [
    OLCI_L1_ASSET_KEYS[0],
    OLCI_L2_LAND_ASSET_KEYS[0],
    OLCI_L2_LAND_ASSET_KEYS_RENAMED[0],
    OLCI_L2_WATER_ASSET_KEYS[0],
    SLSTR_L1_ASSET_KEYS[0],
    SLSTR_L2_FRP_KEYS[0],
    SLSTR_L2_LST_KEYS[0],
    SRAL_L2_LAN_WAT_KEYS[0],
    SYNERGY_SYN_ASSET_KEYS[0],
    SYNERGY_V10_VG1_ASSET_KEYS[0],
    SYNERGY_VGP_ASSET_KEYS[0],
]


@pytest.mark.parametrize(
    "key,expected",
    zip(
        ASSET_KEY_LISTS + ["eopmetadata"],
        [
            "oa01-radiance",
            "ogvi",
            "gifapar",
            "oa01-reflectance",
            "slstr-s1-rad-an",
            "frp-in",
            "lst-in",
            "standard-measurement",
            "syn-oa01-reflectance",
            "b0",
            "b0",
            "eop-metadata",
        ],
    ),
)
def test_kebab_assets(key: str, expected: str) -> None:
    assert stac.sen3_to_kebab(key) == expected


def test_id(ol_1_efr: Path) -> None:
    item = stac.create_item(str(ol_1_efr), skip_nc=True)
    assert item.id == "S3A_OL_1_EFR_20211021T073827_20211021T074112_0164_077_334_4320"
