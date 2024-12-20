from fastapi import Depends

from instorage.main.container.container import Container
from instorage.server.dependencies.container import get_container


def get_info_blob_service(
    container: Container = Depends(get_container(with_user=True)),
):
    return container.info_blob_service()
