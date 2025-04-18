#
# Copyright (c) 2025 Airbyte, Inc., all rights reserved.
#


from typing import Any, Mapping, Optional

from airbyte_cdk.models import ConfiguredAirbyteCatalog, FailureType, SyncMode
from airbyte_cdk.sources.declarative.yaml_declarative_source import YamlDeclarativeSource
from airbyte_cdk.sources.source import TState


class SourceStripe(YamlDeclarativeSource):
    def __init__(self, catalog: Optional[ConfiguredAirbyteCatalog], config: Optional[Mapping[str, Any]], state: TState, **kwargs):
        super().__init__(catalog=catalog, config=config, state=state, **{"path_to_yaml": "manifest.yaml"})
