from pymatgen.ext.matproj import MPRester
from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
import pandas as pd

# Assimilate VASP calculations into ComputedEntry object. Let's assume that
# the calculations are for a series of new LixFeyOz phases that we want to
# know the phase stability.
drone = VaspToComputedEntryDrone()
queen = BorgQueen(drone, rootpath=".")
entries = queen.get_data()

# Obtain all existing Li-Fe-O phases using the Materials Project REST API
with MPRester("NKnnBgWXU5o1S5ogiJGE") as m:
    mp_entries = m.get_entries_in_chemsys(["Mg", "Al", "O"])

# Combined entry from calculated run with Materials Project entries
entries.extend(mp_entries)

# Process entries using the MaterialsProjectCompatibility
compat = MaterialsProjectCompatibility()
entries = compat.process_entries(entries)

# Generate and plot Li-Fe-O phase diagram
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
# plotter.show()

results = m.query("**2O4", ['pretty_formula', 'spacegroup', 'energy'])
print(results)
# df = pd.DataFrame(results)
# df.to_excel('23456.xlsx', sheet_name='Materials_Project', index=False, header=['Structure'], na_rep="NULL")