# Let users know if they're missing any of our hard dependencies
hard_dependencies = ["numpy", "matplotlib"]
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

from backmet.compoundAnnGrowthRate import compoundAnnGrowthRate as compoundAnnGrowthRate
from backmet.sharpeRatio import sharpeRatio as sharpeRatio
from backmet.sharpeRatio import sharpeRatio as sharpeRatio
