from oremda.utils.mpi import OREMDA_MPI_RANK_ENV_VAR, mpi_rank


DEFAULT_OREMDA_VAR_DIR = "/tmp"
DEFAULT_PLASMA_SOCKET_PATH = f"{DEFAULT_OREMDA_VAR_DIR}/plasma_{mpi_rank}.sock"
DEFAULT_DATA_DIR = "/data"
OREMDA_DOCKER_ORG = "oremda"
OREMDA_IMAGE_LABEL_NAME = "oremda.name"
OREMDA_SIF_GLOB_PATTERN = "oremda_*.sif"
SINGULARITY_FROM_LABEL = "org.label-schema.usage.singularity.deffile.from"
