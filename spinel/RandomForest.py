from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.interface_reactions import InterfacialReactivity
from pymatgen.analysis.phase_diagram import PhaseDiagram, GrandPotentialPhaseDiagram
from pymatgen import Composition, Element
# %matplotlib inline

# Initialize the REST API interface. You may need to put your own API key in as an arg.
mpr = MPRester("NKnnBgWXU5o1S5ogiJGE")

# Chemical formulae for two solid reactants.
reactant1 = 'LiCoO2'
reactant2 = 'Li3PS4'

# Is the system open to an elemental reservoir?
grand = True

if grand:
    # Element in the elemental reservoir.
    open_el = 'Co'
    # Relative chemical potential vs. pure substance. Must be non-positive.
    relative_mu = -1

# Get the compositions of the reactants
comp1 = Composition(reactant1)
comp2 = Composition(reactant2)

# Gather all elements involved in the chemical system.
elements = [e.symbol for e in comp1.elements + comp2.elements]
if grand:
    elements.append(open_el)
elements = list(set(elements)) # Remove duplicates

# Get all entries in the chemical system
entries = mpr.get_entries_in_chemsys(elements)

# Build a phase diagram using these entries.
pd = PhaseDiagram(entries)

# For an open system, include the grand potential phase diagram.
if grand:
    # Get the chemical potential of the pure subtance.
    mu = pd.get_transition_chempots(Element(open_el))[0]
    # Set the chemical potential in the elemental reservoir.
    chempots = {open_el: relative_mu + mu}
    # Build the grand potential phase diagram
    gpd = GrandPotentialPhaseDiagram(entries, chempots)
    # Create InterfacialReactivity object.
    interface = InterfacialReactivity(
        comp1, comp2, gpd, norm=True, include_no_mixing_energy=True, pd_non_grand=pd, use_hull_energy=False)
else:
    interface = InterfacialReactivity(
        comp1, comp2, pd, norm=True, include_no_mixing_energy=False, pd_non_grand=None, use_hull_energy=False)

plt = interface.plot()