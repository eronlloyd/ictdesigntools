from dataclasses import dataclass
from typing import Optional
from enum import StrEnum, auto


## Enums and constants

class IECFiberPerformance(StrEnum):
    OM1 = 'OM1'
    OM2 = 'OM2'
    OM3 = 'OM3'
    OM4 = 'OM4'
    OM5 = 'OM5'
    OS1 = 'OS1'
    OS1A = 'OS1A'
    OS2 = 'OS2'

class ITURecommendation(StrEnum):
    G_651_1 = 'G.651.1'
    G_652_A = 'G.652.A'
    G_652_B = 'G.652.B'
    G_652_C = 'G.652.C'
    G_652_D = 'G.652.D'
    G_653 = 'G.653'
    G_654 = 'G.654'
    G_655 = 'G.655'
    G_656 = 'G.656'


SWDM_BANDS = [850, 880, 910, 940]

CWDM_BANDS = [w for w in range(1271, 1612, 20)]

# DWDM bands vary; figure out how to model based on vendor, etc.

## Data classes

@dataclass(frozen=True)
class OpticalConnector:
    name: str


@dataclass(frozen=True)
class Wavelength:
    name: str
    nominal_nm: float
    min_nm: Optional[float] = None
    max_nm: Optional[float] = None


@dataclass(frozen=True)
class OpticalCable:
    name: str
    performance_type: IECFiberPerformance=IECFiberPerformance.OS2
    itu_recommendation: ITURecommendation=ITURecommendation.G_652_D


@dataclass(frozen=True)
class OpticalLane:
    lane_id: int
    name: str
    tx_wavelength: Wavelength
    rx_wavelength: Wavelength
    tx_power_nominal_dbm: float
    tx_power_min_dbm: Optional[float]
    tx_power_max_dbm: Optional[float]
    rx_overload_dbm: Optional[float]     # e.g., -1.0 dBm (or +0.5 dBm)
    rx_sensitivity_dbm: float=-25  # e.g., -14.0 dBm


@dataclass(frozen=True)
class OpticalTransceiver:
    name: str
    

    def __post_init__(self):
        if self.tx_power_min_dbm <= -50:
            raise ValueError("Launch power must be greater than -50 dBm.")
        
        if self.rx_sensitivity_dbm <= -50:
            raise ValueError("Receiver sensitivity must be greater than -50 dBm.")

@dataclass(frozen=True)
class PowerBudget:
    budget: int
    safety_margin: float=2

    def __sub__(self, other: object) -> float:
        # Let the loss budget be subtracted from the power budget
        if isinstance(other, LossBudget):
            return round(self.budget - other.budget, 3)
            
        return NotImplemented