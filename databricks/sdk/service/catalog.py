# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional

from ._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class AccountsCreateMetastore:
    metastore_info: Optional[CreateMetastore] = None

    def as_dict(self) -> dict:
        """Serializes the AccountsCreateMetastore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_info: body['metastore_info'] = self.metastore_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsCreateMetastore:
        """Deserializes the AccountsCreateMetastore from a dictionary."""
        return cls(metastore_info=_from_dict(d, 'metastore_info', CreateMetastore))


@dataclass
class AccountsCreateMetastoreAssignment:
    metastore_assignment: Optional[CreateMetastoreAssignment] = None

    metastore_id: Optional[str] = None
    """Unity Catalog metastore ID"""

    workspace_id: Optional[int] = None
    """Workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the AccountsCreateMetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_assignment: body['metastore_assignment'] = self.metastore_assignment.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsCreateMetastoreAssignment:
        """Deserializes the AccountsCreateMetastoreAssignment from a dictionary."""
        return cls(metastore_assignment=_from_dict(d, 'metastore_assignment', CreateMetastoreAssignment),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class AccountsCreateStorageCredential:
    credential_info: Optional[CreateStorageCredential] = None

    metastore_id: Optional[str] = None
    """Unity Catalog metastore ID"""

    def as_dict(self) -> dict:
        """Serializes the AccountsCreateStorageCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential_info: body['credential_info'] = self.credential_info.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsCreateStorageCredential:
        """Deserializes the AccountsCreateStorageCredential from a dictionary."""
        return cls(credential_info=_from_dict(d, 'credential_info', CreateStorageCredential),
                   metastore_id=d.get('metastore_id', None))


@dataclass
class AccountsMetastoreAssignment:
    metastore_assignment: Optional[MetastoreAssignment] = None

    def as_dict(self) -> dict:
        """Serializes the AccountsMetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_assignment: body['metastore_assignment'] = self.metastore_assignment.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsMetastoreAssignment:
        """Deserializes the AccountsMetastoreAssignment from a dictionary."""
        return cls(metastore_assignment=_from_dict(d, 'metastore_assignment', MetastoreAssignment))


@dataclass
class AccountsMetastoreInfo:
    metastore_info: Optional[MetastoreInfo] = None

    def as_dict(self) -> dict:
        """Serializes the AccountsMetastoreInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_info: body['metastore_info'] = self.metastore_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsMetastoreInfo:
        """Deserializes the AccountsMetastoreInfo from a dictionary."""
        return cls(metastore_info=_from_dict(d, 'metastore_info', MetastoreInfo))


@dataclass
class AccountsStorageCredentialInfo:
    credential_info: Optional[StorageCredentialInfo] = None

    def as_dict(self) -> dict:
        """Serializes the AccountsStorageCredentialInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential_info: body['credential_info'] = self.credential_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsStorageCredentialInfo:
        """Deserializes the AccountsStorageCredentialInfo from a dictionary."""
        return cls(credential_info=_from_dict(d, 'credential_info', StorageCredentialInfo))


@dataclass
class AccountsUpdateMetastore:
    metastore_id: Optional[str] = None
    """Unity Catalog metastore ID"""

    metastore_info: Optional[UpdateMetastore] = None

    def as_dict(self) -> dict:
        """Serializes the AccountsUpdateMetastore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.metastore_info: body['metastore_info'] = self.metastore_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsUpdateMetastore:
        """Deserializes the AccountsUpdateMetastore from a dictionary."""
        return cls(metastore_id=d.get('metastore_id', None),
                   metastore_info=_from_dict(d, 'metastore_info', UpdateMetastore))


@dataclass
class AccountsUpdateMetastoreAssignment:
    metastore_assignment: Optional[UpdateMetastoreAssignment] = None

    metastore_id: Optional[str] = None
    """Unity Catalog metastore ID"""

    workspace_id: Optional[int] = None
    """Workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the AccountsUpdateMetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastore_assignment: body['metastore_assignment'] = self.metastore_assignment.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsUpdateMetastoreAssignment:
        """Deserializes the AccountsUpdateMetastoreAssignment from a dictionary."""
        return cls(metastore_assignment=_from_dict(d, 'metastore_assignment', UpdateMetastoreAssignment),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class AccountsUpdateStorageCredential:
    credential_info: Optional[UpdateStorageCredential] = None

    metastore_id: Optional[str] = None
    """Unity Catalog metastore ID"""

    storage_credential_name: Optional[str] = None
    """Name of the storage credential."""

    def as_dict(self) -> dict:
        """Serializes the AccountsUpdateStorageCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential_info: body['credential_info'] = self.credential_info.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.storage_credential_name is not None:
            body['storage_credential_name'] = self.storage_credential_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AccountsUpdateStorageCredential:
        """Deserializes the AccountsUpdateStorageCredential from a dictionary."""
        return cls(credential_info=_from_dict(d, 'credential_info', UpdateStorageCredential),
                   metastore_id=d.get('metastore_id', None),
                   storage_credential_name=d.get('storage_credential_name', None))


@dataclass
class ArtifactAllowlistInfo:
    artifact_matchers: Optional[List[ArtifactMatcher]] = None
    """A list of allowed artifact match patterns."""

    created_at: Optional[int] = None
    """Time at which this artifact allowlist was set, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of the user who set the artifact allowlist."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    def as_dict(self) -> dict:
        """Serializes the ArtifactAllowlistInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.artifact_matchers: body['artifact_matchers'] = [v.as_dict() for v in self.artifact_matchers]
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ArtifactAllowlistInfo:
        """Deserializes the ArtifactAllowlistInfo from a dictionary."""
        return cls(artifact_matchers=_repeated_dict(d, 'artifact_matchers', ArtifactMatcher),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   metastore_id=d.get('metastore_id', None))


@dataclass
class ArtifactMatcher:
    artifact: str
    """The artifact path or maven coordinate"""

    match_type: MatchType
    """The pattern matching type of the artifact"""

    def as_dict(self) -> dict:
        """Serializes the ArtifactMatcher into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.artifact is not None: body['artifact'] = self.artifact
        if self.match_type is not None: body['match_type'] = self.match_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ArtifactMatcher:
        """Deserializes the ArtifactMatcher from a dictionary."""
        return cls(artifact=d.get('artifact', None), match_type=_enum(d, 'match_type', MatchType))


class ArtifactType(Enum):
    """The artifact type"""

    INIT_SCRIPT = 'INIT_SCRIPT'
    LIBRARY_JAR = 'LIBRARY_JAR'
    LIBRARY_MAVEN = 'LIBRARY_MAVEN'


@dataclass
class AssignResponse:

    def as_dict(self) -> dict:
        """Serializes the AssignResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AssignResponse:
        """Deserializes the AssignResponse from a dictionary."""
        return cls()


@dataclass
class AwsIamRole:
    role_arn: str
    """The Amazon Resource Name (ARN) of the AWS IAM role for S3 data access."""

    external_id: Optional[str] = None
    """The external ID used in role assumption to prevent confused deputy problem.."""

    unity_catalog_iam_arn: Optional[str] = None
    """The Amazon Resource Name (ARN) of the AWS IAM user managed by Databricks. This is the identity
    that is going to assume the AWS IAM role."""

    def as_dict(self) -> dict:
        """Serializes the AwsIamRole into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.external_id is not None: body['external_id'] = self.external_id
        if self.role_arn is not None: body['role_arn'] = self.role_arn
        if self.unity_catalog_iam_arn is not None: body['unity_catalog_iam_arn'] = self.unity_catalog_iam_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AwsIamRole:
        """Deserializes the AwsIamRole from a dictionary."""
        return cls(external_id=d.get('external_id', None),
                   role_arn=d.get('role_arn', None),
                   unity_catalog_iam_arn=d.get('unity_catalog_iam_arn', None))


@dataclass
class AzureManagedIdentity:
    access_connector_id: str
    """The Azure resource ID of the Azure Databricks Access Connector. Use the format
    /subscriptions/{guid}/resourceGroups/{rg-name}/providers/Microsoft.Databricks/accessConnectors/{connector-name}."""

    credential_id: Optional[str] = None
    """The Databricks internal ID that represents this managed identity."""

    managed_identity_id: Optional[str] = None
    """The Azure resource ID of the managed identity. Use the format
    /subscriptions/{guid}/resourceGroups/{rg-name}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identity-name}.
    This is only available for user-assgined identities. For system-assigned identities, the
    access_connector_id is used to identify the identity. If this field is not provided, then we
    assume the AzureManagedIdentity is for a system-assigned identity."""

    def as_dict(self) -> dict:
        """Serializes the AzureManagedIdentity into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_connector_id is not None: body['access_connector_id'] = self.access_connector_id
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.managed_identity_id is not None: body['managed_identity_id'] = self.managed_identity_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AzureManagedIdentity:
        """Deserializes the AzureManagedIdentity from a dictionary."""
        return cls(access_connector_id=d.get('access_connector_id', None),
                   credential_id=d.get('credential_id', None),
                   managed_identity_id=d.get('managed_identity_id', None))


@dataclass
class AzureServicePrincipal:
    directory_id: str
    """The directory ID corresponding to the Azure Active Directory (AAD) tenant of the application."""

    application_id: str
    """The application ID of the application registration within the referenced AAD tenant."""

    client_secret: str
    """The client secret generated for the above app ID in AAD."""

    def as_dict(self) -> dict:
        """Serializes the AzureServicePrincipal into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.application_id is not None: body['application_id'] = self.application_id
        if self.client_secret is not None: body['client_secret'] = self.client_secret
        if self.directory_id is not None: body['directory_id'] = self.directory_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AzureServicePrincipal:
        """Deserializes the AzureServicePrincipal from a dictionary."""
        return cls(application_id=d.get('application_id', None),
                   client_secret=d.get('client_secret', None),
                   directory_id=d.get('directory_id', None))


@dataclass
class CancelRefreshResponse:

    def as_dict(self) -> dict:
        """Serializes the CancelRefreshResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CancelRefreshResponse:
        """Deserializes the CancelRefreshResponse from a dictionary."""
        return cls()


@dataclass
class CatalogInfo:
    browse_only: Optional[bool] = None
    """Indicate whether or not the catalog info contains only browsable metadata."""

    catalog_type: Optional[CatalogType] = None
    """The type of the catalog."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    connection_name: Optional[str] = None
    """The name of the connection to an external data source."""

    created_at: Optional[int] = None
    """Time at which this catalog was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of catalog creator."""

    effective_predictive_optimization_flag: Optional[EffectivePredictiveOptimizationFlag] = None

    enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None
    """Whether predictive optimization should be enabled for this object and objects under it."""

    full_name: Optional[str] = None
    """The full name of the catalog. Corresponds with the name field."""

    isolation_mode: Optional[IsolationMode] = None
    """Whether the current securable is accessible from all workspaces or a specific set of workspaces."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """Name of catalog."""

    options: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    owner: Optional[str] = None
    """Username of current owner of catalog."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    provider_name: Optional[str] = None
    """The name of delta sharing provider.
    
    A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server."""

    provisioning_info: Optional[ProvisioningInfo] = None
    """Status of an asynchronously provisioned resource."""

    securable_kind: Optional[CatalogInfoSecurableKind] = None
    """Kind of catalog securable."""

    securable_type: Optional[str] = None

    share_name: Optional[str] = None
    """The name of the share under the share provider."""

    storage_location: Optional[str] = None
    """Storage Location URL (full path) for managed tables within catalog."""

    storage_root: Optional[str] = None
    """Storage root URL for managed tables within catalog."""

    updated_at: Optional[int] = None
    """Time at which this catalog was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified catalog."""

    def as_dict(self) -> dict:
        """Serializes the CatalogInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.browse_only is not None: body['browse_only'] = self.browse_only
        if self.catalog_type is not None: body['catalog_type'] = self.catalog_type.value
        if self.comment is not None: body['comment'] = self.comment
        if self.connection_name is not None: body['connection_name'] = self.connection_name
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.effective_predictive_optimization_flag:
            body[
                'effective_predictive_optimization_flag'] = self.effective_predictive_optimization_flag.as_dict(
                )
        if self.enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = self.enable_predictive_optimization.value
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.isolation_mode is not None: body['isolation_mode'] = self.isolation_mode.value
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.owner is not None: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.provider_name is not None: body['provider_name'] = self.provider_name
        if self.provisioning_info: body['provisioning_info'] = self.provisioning_info.as_dict()
        if self.securable_kind is not None: body['securable_kind'] = self.securable_kind.value
        if self.securable_type is not None: body['securable_type'] = self.securable_type
        if self.share_name is not None: body['share_name'] = self.share_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CatalogInfo:
        """Deserializes the CatalogInfo from a dictionary."""
        return cls(browse_only=d.get('browse_only', None),
                   catalog_type=_enum(d, 'catalog_type', CatalogType),
                   comment=d.get('comment', None),
                   connection_name=d.get('connection_name', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   effective_predictive_optimization_flag=_from_dict(
                       d, 'effective_predictive_optimization_flag', EffectivePredictiveOptimizationFlag),
                   enable_predictive_optimization=_enum(d, 'enable_predictive_optimization',
                                                        EnablePredictiveOptimization),
                   full_name=d.get('full_name', None),
                   isolation_mode=_enum(d, 'isolation_mode', IsolationMode),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   provider_name=d.get('provider_name', None),
                   provisioning_info=_from_dict(d, 'provisioning_info', ProvisioningInfo),
                   securable_kind=_enum(d, 'securable_kind', CatalogInfoSecurableKind),
                   securable_type=d.get('securable_type', None),
                   share_name=d.get('share_name', None),
                   storage_location=d.get('storage_location', None),
                   storage_root=d.get('storage_root', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class CatalogInfoSecurableKind(Enum):
    """Kind of catalog securable."""

    CATALOG_DELTASHARING = 'CATALOG_DELTASHARING'
    CATALOG_FOREIGN_BIGQUERY = 'CATALOG_FOREIGN_BIGQUERY'
    CATALOG_FOREIGN_DATABRICKS = 'CATALOG_FOREIGN_DATABRICKS'
    CATALOG_FOREIGN_MYSQL = 'CATALOG_FOREIGN_MYSQL'
    CATALOG_FOREIGN_POSTGRESQL = 'CATALOG_FOREIGN_POSTGRESQL'
    CATALOG_FOREIGN_REDSHIFT = 'CATALOG_FOREIGN_REDSHIFT'
    CATALOG_FOREIGN_SNOWFLAKE = 'CATALOG_FOREIGN_SNOWFLAKE'
    CATALOG_FOREIGN_SQLDW = 'CATALOG_FOREIGN_SQLDW'
    CATALOG_FOREIGN_SQLSERVER = 'CATALOG_FOREIGN_SQLSERVER'
    CATALOG_INTERNAL = 'CATALOG_INTERNAL'
    CATALOG_ONLINE = 'CATALOG_ONLINE'
    CATALOG_ONLINE_INDEX = 'CATALOG_ONLINE_INDEX'
    CATALOG_STANDARD = 'CATALOG_STANDARD'
    CATALOG_SYSTEM = 'CATALOG_SYSTEM'
    CATALOG_SYSTEM_DELTASHARING = 'CATALOG_SYSTEM_DELTASHARING'


class CatalogType(Enum):
    """The type of the catalog."""

    DELTASHARING_CATALOG = 'DELTASHARING_CATALOG'
    MANAGED_CATALOG = 'MANAGED_CATALOG'
    SYSTEM_CATALOG = 'SYSTEM_CATALOG'


@dataclass
class CloudflareApiToken:
    access_key_id: str
    """The Cloudflare access key id of the token."""

    secret_access_key: str
    """The secret access token generated for the access key id"""

    account_id: str
    """The account id associated with the API token."""

    def as_dict(self) -> dict:
        """Serializes the CloudflareApiToken into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_key_id is not None: body['access_key_id'] = self.access_key_id
        if self.account_id is not None: body['account_id'] = self.account_id
        if self.secret_access_key is not None: body['secret_access_key'] = self.secret_access_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CloudflareApiToken:
        """Deserializes the CloudflareApiToken from a dictionary."""
        return cls(access_key_id=d.get('access_key_id', None),
                   account_id=d.get('account_id', None),
                   secret_access_key=d.get('secret_access_key', None))


@dataclass
class ColumnInfo:
    comment: Optional[str] = None
    """User-provided free-form text description."""

    mask: Optional[ColumnMask] = None

    name: Optional[str] = None
    """Name of Column."""

    nullable: Optional[bool] = None
    """Whether field may be Null (default: true)."""

    partition_index: Optional[int] = None
    """Partition index for column."""

    position: Optional[int] = None
    """Ordinal position of column (starting at position 0)."""

    type_interval_type: Optional[str] = None
    """Format of IntervalType."""

    type_json: Optional[str] = None
    """Full data type specification, JSON-serialized."""

    type_name: Optional[ColumnTypeName] = None
    """Name of type (INT, STRUCT, MAP, etc.)."""

    type_precision: Optional[int] = None
    """Digits of precision; required for DecimalTypes."""

    type_scale: Optional[int] = None
    """Digits to right of decimal; Required for DecimalTypes."""

    type_text: Optional[str] = None
    """Full data type specification as SQL/catalogString text."""

    def as_dict(self) -> dict:
        """Serializes the ColumnInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.mask: body['mask'] = self.mask.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.nullable is not None: body['nullable'] = self.nullable
        if self.partition_index is not None: body['partition_index'] = self.partition_index
        if self.position is not None: body['position'] = self.position
        if self.type_interval_type is not None: body['type_interval_type'] = self.type_interval_type
        if self.type_json is not None: body['type_json'] = self.type_json
        if self.type_name is not None: body['type_name'] = self.type_name.value
        if self.type_precision is not None: body['type_precision'] = self.type_precision
        if self.type_scale is not None: body['type_scale'] = self.type_scale
        if self.type_text is not None: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ColumnInfo:
        """Deserializes the ColumnInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   mask=_from_dict(d, 'mask', ColumnMask),
                   name=d.get('name', None),
                   nullable=d.get('nullable', None),
                   partition_index=d.get('partition_index', None),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_json=d.get('type_json', None),
                   type_name=_enum(d, 'type_name', ColumnTypeName),
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


@dataclass
class ColumnMask:
    function_name: Optional[str] = None
    """The full name of the column mask SQL UDF."""

    using_column_names: Optional[List[str]] = None
    """The list of additional table columns to be passed as input to the column mask function. The
    first arg of the mask function should be of the type of the column being masked and the types of
    the rest of the args should match the types of columns in 'using_column_names'."""

    def as_dict(self) -> dict:
        """Serializes the ColumnMask into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.function_name is not None: body['function_name'] = self.function_name
        if self.using_column_names: body['using_column_names'] = [v for v in self.using_column_names]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ColumnMask:
        """Deserializes the ColumnMask from a dictionary."""
        return cls(function_name=d.get('function_name', None),
                   using_column_names=d.get('using_column_names', None))


class ColumnTypeName(Enum):
    """Name of type (INT, STRUCT, MAP, etc.)."""

    ARRAY = 'ARRAY'
    BINARY = 'BINARY'
    BOOLEAN = 'BOOLEAN'
    BYTE = 'BYTE'
    CHAR = 'CHAR'
    DATE = 'DATE'
    DECIMAL = 'DECIMAL'
    DOUBLE = 'DOUBLE'
    FLOAT = 'FLOAT'
    INT = 'INT'
    INTERVAL = 'INTERVAL'
    LONG = 'LONG'
    MAP = 'MAP'
    NULL = 'NULL'
    SHORT = 'SHORT'
    STRING = 'STRING'
    STRUCT = 'STRUCT'
    TABLE_TYPE = 'TABLE_TYPE'
    TIMESTAMP = 'TIMESTAMP'
    TIMESTAMP_NTZ = 'TIMESTAMP_NTZ'
    USER_DEFINED_TYPE = 'USER_DEFINED_TYPE'


@dataclass
class ConnectionInfo:
    comment: Optional[str] = None
    """User-provided free-form text description."""

    connection_id: Optional[str] = None
    """Unique identifier of the Connection."""

    connection_type: Optional[ConnectionType] = None
    """The type of connection."""

    created_at: Optional[int] = None
    """Time at which this connection was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of connection creator."""

    credential_type: Optional[CredentialType] = None
    """The type of credential."""

    full_name: Optional[str] = None
    """Full name of connection."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """Name of the connection."""

    options: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    owner: Optional[str] = None
    """Username of current owner of the connection."""

    properties: Optional[Dict[str, str]] = None
    """An object containing map of key-value properties attached to the connection."""

    provisioning_info: Optional[ProvisioningInfo] = None
    """Status of an asynchronously provisioned resource."""

    read_only: Optional[bool] = None
    """If the connection is read only."""

    securable_kind: Optional[ConnectionInfoSecurableKind] = None
    """Kind of connection securable."""

    securable_type: Optional[str] = None

    updated_at: Optional[int] = None
    """Time at which this connection was updated, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified connection."""

    url: Optional[str] = None
    """URL of the remote data source, extracted from options."""

    def as_dict(self) -> dict:
        """Serializes the ConnectionInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.connection_id is not None: body['connection_id'] = self.connection_id
        if self.connection_type is not None: body['connection_type'] = self.connection_type.value
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.credential_type is not None: body['credential_type'] = self.credential_type.value
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.owner is not None: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.provisioning_info: body['provisioning_info'] = self.provisioning_info.as_dict()
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.securable_kind is not None: body['securable_kind'] = self.securable_kind.value
        if self.securable_type is not None: body['securable_type'] = self.securable_type
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ConnectionInfo:
        """Deserializes the ConnectionInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   connection_id=d.get('connection_id', None),
                   connection_type=_enum(d, 'connection_type', ConnectionType),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   credential_type=_enum(d, 'credential_type', CredentialType),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   provisioning_info=_from_dict(d, 'provisioning_info', ProvisioningInfo),
                   read_only=d.get('read_only', None),
                   securable_kind=_enum(d, 'securable_kind', ConnectionInfoSecurableKind),
                   securable_type=d.get('securable_type', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   url=d.get('url', None))


class ConnectionInfoSecurableKind(Enum):
    """Kind of connection securable."""

    CONNECTION_BIGQUERY = 'CONNECTION_BIGQUERY'
    CONNECTION_DATABRICKS = 'CONNECTION_DATABRICKS'
    CONNECTION_MYSQL = 'CONNECTION_MYSQL'
    CONNECTION_ONLINE_CATALOG = 'CONNECTION_ONLINE_CATALOG'
    CONNECTION_POSTGRESQL = 'CONNECTION_POSTGRESQL'
    CONNECTION_REDSHIFT = 'CONNECTION_REDSHIFT'
    CONNECTION_SNOWFLAKE = 'CONNECTION_SNOWFLAKE'
    CONNECTION_SQLDW = 'CONNECTION_SQLDW'
    CONNECTION_SQLSERVER = 'CONNECTION_SQLSERVER'


class ConnectionType(Enum):
    """The type of connection."""

    BIGQUERY = 'BIGQUERY'
    DATABRICKS = 'DATABRICKS'
    MYSQL = 'MYSQL'
    POSTGRESQL = 'POSTGRESQL'
    REDSHIFT = 'REDSHIFT'
    SNOWFLAKE = 'SNOWFLAKE'
    SQLDW = 'SQLDW'
    SQLSERVER = 'SQLSERVER'


@dataclass
class ContinuousUpdateStatus:
    """Detailed status of an online table. Shown if the online table is in the ONLINE_CONTINUOUS_UPDATE
    or the ONLINE_UPDATING_PIPELINE_RESOURCES state."""

    initial_pipeline_sync_progress: Optional[PipelineProgress] = None
    """Progress of the initial data synchronization."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the online table. Note that this Delta
    version may not be completely synced to the online table yet."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the online
    table."""

    def as_dict(self) -> dict:
        """Serializes the ContinuousUpdateStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body['initial_pipeline_sync_progress'] = self.initial_pipeline_sync_progress.as_dict()
        if self.last_processed_commit_version is not None:
            body['last_processed_commit_version'] = self.last_processed_commit_version
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ContinuousUpdateStatus:
        """Deserializes the ContinuousUpdateStatus from a dictionary."""
        return cls(initial_pipeline_sync_progress=_from_dict(d, 'initial_pipeline_sync_progress',
                                                             PipelineProgress),
                   last_processed_commit_version=d.get('last_processed_commit_version', None),
                   timestamp=d.get('timestamp', None))


@dataclass
class CreateCatalog:
    name: str
    """Name of catalog."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    connection_name: Optional[str] = None
    """The name of the connection to an external data source."""

    options: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    provider_name: Optional[str] = None
    """The name of delta sharing provider.
    
    A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server."""

    share_name: Optional[str] = None
    """The name of the share under the share provider."""

    storage_root: Optional[str] = None
    """Storage root URL for managed tables within catalog."""

    def as_dict(self) -> dict:
        """Serializes the CreateCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.connection_name is not None: body['connection_name'] = self.connection_name
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.properties: body['properties'] = self.properties
        if self.provider_name is not None: body['provider_name'] = self.provider_name
        if self.share_name is not None: body['share_name'] = self.share_name
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateCatalog:
        """Deserializes the CreateCatalog from a dictionary."""
        return cls(comment=d.get('comment', None),
                   connection_name=d.get('connection_name', None),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   properties=d.get('properties', None),
                   provider_name=d.get('provider_name', None),
                   share_name=d.get('share_name', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateConnection:
    name: str
    """Name of the connection."""

    connection_type: ConnectionType
    """The type of connection."""

    options: Dict[str, str]
    """A map of key-value properties attached to the securable."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    properties: Optional[Dict[str, str]] = None
    """An object containing map of key-value properties attached to the connection."""

    read_only: Optional[bool] = None
    """If the connection is read only."""

    def as_dict(self) -> dict:
        """Serializes the CreateConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.connection_type is not None: body['connection_type'] = self.connection_type.value
        if self.name is not None: body['name'] = self.name
        if self.options: body['options'] = self.options
        if self.properties: body['properties'] = self.properties
        if self.read_only is not None: body['read_only'] = self.read_only
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateConnection:
        """Deserializes the CreateConnection from a dictionary."""
        return cls(comment=d.get('comment', None),
                   connection_type=_enum(d, 'connection_type', ConnectionType),
                   name=d.get('name', None),
                   options=d.get('options', None),
                   properties=d.get('properties', None),
                   read_only=d.get('read_only', None))


@dataclass
class CreateExternalLocation:
    name: str
    """Name of the external location."""

    url: str
    """Path URL of the external location."""

    credential_name: str
    """Name of the storage credential used with this location."""

    access_point: Optional[str] = None
    """The AWS access point to use when accesing s3 for this external location."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    encryption_details: Optional[EncryptionDetails] = None
    """Encryption options that apply to clients connecting to cloud storage."""

    read_only: Optional[bool] = None
    """Indicates whether the external location is read-only."""

    skip_validation: Optional[bool] = None
    """Skips validation of the storage credential associated with the external location."""

    def as_dict(self) -> dict:
        """Serializes the CreateExternalLocation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_point is not None: body['access_point'] = self.access_point
        if self.comment is not None: body['comment'] = self.comment
        if self.credential_name is not None: body['credential_name'] = self.credential_name
        if self.encryption_details: body['encryption_details'] = self.encryption_details.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.skip_validation is not None: body['skip_validation'] = self.skip_validation
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateExternalLocation:
        """Deserializes the CreateExternalLocation from a dictionary."""
        return cls(access_point=d.get('access_point', None),
                   comment=d.get('comment', None),
                   credential_name=d.get('credential_name', None),
                   encryption_details=_from_dict(d, 'encryption_details', EncryptionDetails),
                   name=d.get('name', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None),
                   url=d.get('url', None))


@dataclass
class CreateFunction:
    name: str
    """Name of function, relative to parent schema."""

    catalog_name: str
    """Name of parent catalog."""

    schema_name: str
    """Name of parent schema relative to its parent catalog."""

    input_params: FunctionParameterInfos

    data_type: ColumnTypeName
    """Scalar function return data type."""

    full_data_type: str
    """Pretty printed function data type."""

    return_params: FunctionParameterInfos
    """Table function return parameters."""

    routine_body: CreateFunctionRoutineBody
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    routine_definition: str
    """Function body."""

    routine_dependencies: DependencyList
    """Function dependencies."""

    parameter_style: CreateFunctionParameterStyle
    """Function parameter style. **S** is the value for SQL."""

    is_deterministic: bool
    """Whether the function is deterministic."""

    sql_data_access: CreateFunctionSqlDataAccess
    """Function SQL data access."""

    is_null_call: bool
    """Function null call."""

    security_type: CreateFunctionSecurityType
    """Function security type."""

    specific_name: str
    """Specific name of the function; Reserved for future use."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    external_language: Optional[str] = None
    """External function language."""

    external_name: Optional[str] = None
    """External function name."""

    properties: Optional[str] = None
    """JSON-serialized key-value pair map, encoded (escaped) as a string."""

    sql_path: Optional[str] = None
    """List of schemes whose objects can be referenced without qualification."""

    def as_dict(self) -> dict:
        """Serializes the CreateFunction into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.data_type is not None: body['data_type'] = self.data_type.value
        if self.external_language is not None: body['external_language'] = self.external_language
        if self.external_name is not None: body['external_name'] = self.external_name
        if self.full_data_type is not None: body['full_data_type'] = self.full_data_type
        if self.input_params: body['input_params'] = self.input_params.as_dict()
        if self.is_deterministic is not None: body['is_deterministic'] = self.is_deterministic
        if self.is_null_call is not None: body['is_null_call'] = self.is_null_call
        if self.name is not None: body['name'] = self.name
        if self.parameter_style is not None: body['parameter_style'] = self.parameter_style.value
        if self.properties is not None: body['properties'] = self.properties
        if self.return_params: body['return_params'] = self.return_params.as_dict()
        if self.routine_body is not None: body['routine_body'] = self.routine_body.value
        if self.routine_definition is not None: body['routine_definition'] = self.routine_definition
        if self.routine_dependencies: body['routine_dependencies'] = self.routine_dependencies.as_dict()
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.security_type is not None: body['security_type'] = self.security_type.value
        if self.specific_name is not None: body['specific_name'] = self.specific_name
        if self.sql_data_access is not None: body['sql_data_access'] = self.sql_data_access.value
        if self.sql_path is not None: body['sql_path'] = self.sql_path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateFunction:
        """Deserializes the CreateFunction from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   data_type=_enum(d, 'data_type', ColumnTypeName),
                   external_language=d.get('external_language', None),
                   external_name=d.get('external_name', None),
                   full_data_type=d.get('full_data_type', None),
                   input_params=_from_dict(d, 'input_params', FunctionParameterInfos),
                   is_deterministic=d.get('is_deterministic', None),
                   is_null_call=d.get('is_null_call', None),
                   name=d.get('name', None),
                   parameter_style=_enum(d, 'parameter_style', CreateFunctionParameterStyle),
                   properties=d.get('properties', None),
                   return_params=_from_dict(d, 'return_params', FunctionParameterInfos),
                   routine_body=_enum(d, 'routine_body', CreateFunctionRoutineBody),
                   routine_definition=d.get('routine_definition', None),
                   routine_dependencies=_from_dict(d, 'routine_dependencies', DependencyList),
                   schema_name=d.get('schema_name', None),
                   security_type=_enum(d, 'security_type', CreateFunctionSecurityType),
                   specific_name=d.get('specific_name', None),
                   sql_data_access=_enum(d, 'sql_data_access', CreateFunctionSqlDataAccess),
                   sql_path=d.get('sql_path', None))


class CreateFunctionParameterStyle(Enum):
    """Function parameter style. **S** is the value for SQL."""

    S = 'S'


@dataclass
class CreateFunctionRequest:
    function_info: CreateFunction
    """Partial __FunctionInfo__ specifying the function to be created."""

    def as_dict(self) -> dict:
        """Serializes the CreateFunctionRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.function_info: body['function_info'] = self.function_info.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateFunctionRequest:
        """Deserializes the CreateFunctionRequest from a dictionary."""
        return cls(function_info=_from_dict(d, 'function_info', CreateFunction))


class CreateFunctionRoutineBody(Enum):
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    EXTERNAL = 'EXTERNAL'
    SQL = 'SQL'


class CreateFunctionSecurityType(Enum):
    """Function security type."""

    DEFINER = 'DEFINER'


class CreateFunctionSqlDataAccess(Enum):
    """Function SQL data access."""

    CONTAINS_SQL = 'CONTAINS_SQL'
    NO_SQL = 'NO_SQL'
    READS_SQL_DATA = 'READS_SQL_DATA'


@dataclass
class CreateMetastore:
    name: str
    """The user-specified name of the metastore."""

    region: Optional[str] = None
    """Cloud region which the metastore serves (e.g., `us-west-2`, `westus`). If this field is omitted,
    the region of the workspace receiving the request will be used."""

    storage_root: Optional[str] = None
    """The storage root URL for metastore"""

    def as_dict(self) -> dict:
        """Serializes the CreateMetastore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.region is not None: body['region'] = self.region
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateMetastore:
        """Deserializes the CreateMetastore from a dictionary."""
        return cls(name=d.get('name', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateMetastoreAssignment:
    metastore_id: str
    """The unique ID of the metastore."""

    default_catalog_name: str
    """The name of the default catalog in the metastore."""

    workspace_id: Optional[int] = None
    """A workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the CreateMetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_catalog_name is not None: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateMetastoreAssignment:
        """Deserializes the CreateMetastoreAssignment from a dictionary."""
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class CreateMonitor:
    assets_dir: str
    """The directory to store monitoring assets (e.g. dashboard, metric tables)."""

    output_schema_name: str
    """Schema where output metric tables are created."""

    baseline_table_name: Optional[str] = None
    """Name of the baseline table from which drift metrics are computed from. Columns in the monitored
    table should also be present in the baseline table."""

    custom_metrics: Optional[List[MonitorCustomMetric]] = None
    """Custom metrics to compute on the monitored table. These can be aggregate metrics, derived
    metrics (from already computed aggregate metrics), or drift metrics (comparing metrics across
    time windows)."""

    data_classification_config: Optional[MonitorDataClassificationConfig] = None
    """The data classification config for the monitor."""

    full_name: Optional[str] = None
    """Full name of the table."""

    inference_log: Optional[MonitorInferenceLogProfileType] = None
    """Configuration for monitoring inference logs."""

    notifications: Optional[List[MonitorNotificationsConfig]] = None
    """The notification settings for the monitor."""

    schedule: Optional[MonitorCronSchedule] = None
    """The schedule for automatically updating and refreshing metric tables."""

    skip_builtin_dashboard: Optional[bool] = None
    """Whether to skip creating a default dashboard summarizing data quality metrics."""

    slicing_exprs: Optional[List[str]] = None
    """List of column expressions to slice data with for targeted analysis. The data is grouped by each
    expression independently, resulting in a separate slice for each predicate and its complements.
    For high-cardinality columns, only the top 100 unique values by frequency will generate slices."""

    snapshot: Optional[MonitorSnapshotProfileType] = None
    """Configuration for monitoring snapshot tables."""

    time_series: Optional[MonitorTimeSeriesProfileType] = None
    """Configuration for monitoring time series tables."""

    warehouse_id: Optional[str] = None
    """Optional argument to specify the warehouse for dashboard creation. If not specified, the first
    running warehouse will be used."""

    def as_dict(self) -> dict:
        """Serializes the CreateMonitor into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.assets_dir is not None: body['assets_dir'] = self.assets_dir
        if self.baseline_table_name is not None: body['baseline_table_name'] = self.baseline_table_name
        if self.custom_metrics: body['custom_metrics'] = [v.as_dict() for v in self.custom_metrics]
        if self.data_classification_config:
            body['data_classification_config'] = self.data_classification_config.as_dict()
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.inference_log: body['inference_log'] = self.inference_log.as_dict()
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.output_schema_name is not None: body['output_schema_name'] = self.output_schema_name
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.skip_builtin_dashboard is not None:
            body['skip_builtin_dashboard'] = self.skip_builtin_dashboard
        if self.slicing_exprs: body['slicing_exprs'] = [v for v in self.slicing_exprs]
        if self.snapshot: body['snapshot'] = self.snapshot.as_dict()
        if self.time_series: body['time_series'] = self.time_series.as_dict()
        if self.warehouse_id is not None: body['warehouse_id'] = self.warehouse_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateMonitor:
        """Deserializes the CreateMonitor from a dictionary."""
        return cls(assets_dir=d.get('assets_dir', None),
                   baseline_table_name=d.get('baseline_table_name', None),
                   custom_metrics=_repeated_dict(d, 'custom_metrics', MonitorCustomMetric),
                   data_classification_config=_from_dict(d, 'data_classification_config',
                                                         MonitorDataClassificationConfig),
                   full_name=d.get('full_name', None),
                   inference_log=_from_dict(d, 'inference_log', MonitorInferenceLogProfileType),
                   notifications=_repeated_dict(d, 'notifications', MonitorNotificationsConfig),
                   output_schema_name=d.get('output_schema_name', None),
                   schedule=_from_dict(d, 'schedule', MonitorCronSchedule),
                   skip_builtin_dashboard=d.get('skip_builtin_dashboard', None),
                   slicing_exprs=d.get('slicing_exprs', None),
                   snapshot=_from_dict(d, 'snapshot', MonitorSnapshotProfileType),
                   time_series=_from_dict(d, 'time_series', MonitorTimeSeriesProfileType),
                   warehouse_id=d.get('warehouse_id', None))


@dataclass
class CreateRegisteredModelRequest:
    catalog_name: str
    """The name of the catalog where the schema and the registered model reside"""

    schema_name: str
    """The name of the schema where the registered model resides"""

    name: str
    """The name of the registered model"""

    comment: Optional[str] = None
    """The comment attached to the registered model"""

    storage_location: Optional[str] = None
    """The storage location on the cloud under which model version data files are stored"""

    def as_dict(self) -> dict:
        """Serializes the CreateRegisteredModelRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateRegisteredModelRequest:
        """Deserializes the CreateRegisteredModelRequest from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   schema_name=d.get('schema_name', None),
                   storage_location=d.get('storage_location', None))


@dataclass
class CreateResponse:

    def as_dict(self) -> dict:
        """Serializes the CreateResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateResponse:
        """Deserializes the CreateResponse from a dictionary."""
        return cls()


@dataclass
class CreateSchema:
    name: str
    """Name of schema, relative to parent catalog."""

    catalog_name: str
    """Name of parent catalog."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    storage_root: Optional[str] = None
    """Storage root URL for managed tables within schema."""

    def as_dict(self) -> dict:
        """Serializes the CreateSchema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.properties: body['properties'] = self.properties
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateSchema:
        """Deserializes the CreateSchema from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   properties=d.get('properties', None),
                   storage_root=d.get('storage_root', None))


@dataclass
class CreateStorageCredential:
    name: str
    """The credential name. The name must be unique within the metastore."""

    aws_iam_role: Optional[AwsIamRole] = None
    """The AWS IAM role configuration."""

    azure_managed_identity: Optional[AzureManagedIdentity] = None
    """The Azure managed identity configuration."""

    azure_service_principal: Optional[AzureServicePrincipal] = None
    """The Azure service principal configuration."""

    cloudflare_api_token: Optional[CloudflareApiToken] = None
    """The Cloudflare API token configuration."""

    comment: Optional[str] = None
    """Comment associated with the credential."""

    databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None
    """The <Databricks> managed GCP service account configuration."""

    read_only: Optional[bool] = None
    """Whether the storage credential is only usable for read operations."""

    skip_validation: Optional[bool] = None
    """Supplying true to this argument skips validation of the created credential."""

    def as_dict(self) -> dict:
        """Serializes the CreateStorageCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_managed_identity: body['azure_managed_identity'] = self.azure_managed_identity.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.cloudflare_api_token: body['cloudflare_api_token'] = self.cloudflare_api_token.as_dict()
        if self.comment is not None: body['comment'] = self.comment
        if self.databricks_gcp_service_account:
            body['databricks_gcp_service_account'] = self.databricks_gcp_service_account.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.skip_validation is not None: body['skip_validation'] = self.skip_validation
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateStorageCredential:
        """Deserializes the CreateStorageCredential from a dictionary."""
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_managed_identity=_from_dict(d, 'azure_managed_identity', AzureManagedIdentity),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   cloudflare_api_token=_from_dict(d, 'cloudflare_api_token', CloudflareApiToken),
                   comment=d.get('comment', None),
                   databricks_gcp_service_account=_from_dict(d, 'databricks_gcp_service_account',
                                                             DatabricksGcpServiceAccountRequest),
                   name=d.get('name', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None))


@dataclass
class CreateTableConstraint:
    full_name_arg: str
    """The full name of the table referenced by the constraint."""

    constraint: TableConstraint
    """A table constraint, as defined by *one* of the following fields being set:
    __primary_key_constraint__, __foreign_key_constraint__, __named_table_constraint__."""

    def as_dict(self) -> dict:
        """Serializes the CreateTableConstraint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.constraint: body['constraint'] = self.constraint.as_dict()
        if self.full_name_arg is not None: body['full_name_arg'] = self.full_name_arg
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateTableConstraint:
        """Deserializes the CreateTableConstraint from a dictionary."""
        return cls(constraint=_from_dict(d, 'constraint', TableConstraint),
                   full_name_arg=d.get('full_name_arg', None))


@dataclass
class CreateVolumeRequestContent:
    catalog_name: str
    """The name of the catalog where the schema and the volume are"""

    schema_name: str
    """The name of the schema where the volume is"""

    name: str
    """The name of the volume"""

    volume_type: VolumeType

    comment: Optional[str] = None
    """The comment attached to the volume"""

    storage_location: Optional[str] = None
    """The storage location on the cloud"""

    def as_dict(self) -> dict:
        """Serializes the CreateVolumeRequestContent into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.volume_type is not None: body['volume_type'] = self.volume_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateVolumeRequestContent:
        """Deserializes the CreateVolumeRequestContent from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   name=d.get('name', None),
                   schema_name=d.get('schema_name', None),
                   storage_location=d.get('storage_location', None),
                   volume_type=_enum(d, 'volume_type', VolumeType))


class CredentialType(Enum):
    """The type of credential."""

    USERNAME_PASSWORD = 'USERNAME_PASSWORD'


@dataclass
class CurrentWorkspaceBindings:
    """Currently assigned workspaces"""

    workspaces: Optional[List[int]] = None
    """A list of workspace IDs."""

    def as_dict(self) -> dict:
        """Serializes the CurrentWorkspaceBindings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.workspaces: body['workspaces'] = [v for v in self.workspaces]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CurrentWorkspaceBindings:
        """Deserializes the CurrentWorkspaceBindings from a dictionary."""
        return cls(workspaces=d.get('workspaces', None))


class DataSourceFormat(Enum):
    """Data source format"""

    AVRO = 'AVRO'
    CSV = 'CSV'
    DELTA = 'DELTA'
    DELTASHARING = 'DELTASHARING'
    JSON = 'JSON'
    ORC = 'ORC'
    PARQUET = 'PARQUET'
    TEXT = 'TEXT'
    UNITY_CATALOG = 'UNITY_CATALOG'


@dataclass
class DatabricksGcpServiceAccountRequest:

    def as_dict(self) -> dict:
        """Serializes the DatabricksGcpServiceAccountRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DatabricksGcpServiceAccountRequest:
        """Deserializes the DatabricksGcpServiceAccountRequest from a dictionary."""
        return cls()


@dataclass
class DatabricksGcpServiceAccountResponse:
    credential_id: Optional[str] = None
    """The Databricks internal ID that represents this service account. This is an output-only field."""

    email: Optional[str] = None
    """The email of the service account. This is an output-only field."""

    def as_dict(self) -> dict:
        """Serializes the DatabricksGcpServiceAccountResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.email is not None: body['email'] = self.email
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DatabricksGcpServiceAccountResponse:
        """Deserializes the DatabricksGcpServiceAccountResponse from a dictionary."""
        return cls(credential_id=d.get('credential_id', None), email=d.get('email', None))


@dataclass
class DeleteAliasResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteAliasResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteAliasResponse:
        """Deserializes the DeleteAliasResponse from a dictionary."""
        return cls()


@dataclass
class DeleteResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


@dataclass
class DeltaRuntimePropertiesKvPairs:
    """Properties pertaining to the current state of the delta table as given by the commit server.
    This does not contain **delta.*** (input) properties in __TableInfo.properties__."""

    delta_runtime_properties: Dict[str, str]
    """A map of key-value properties attached to the securable."""

    def as_dict(self) -> dict:
        """Serializes the DeltaRuntimePropertiesKvPairs into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delta_runtime_properties: body['delta_runtime_properties'] = self.delta_runtime_properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeltaRuntimePropertiesKvPairs:
        """Deserializes the DeltaRuntimePropertiesKvPairs from a dictionary."""
        return cls(delta_runtime_properties=d.get('delta_runtime_properties', None))


@dataclass
class Dependency:
    """A dependency of a SQL object. Either the __table__ field or the __function__ field must be
    defined."""

    function: Optional[FunctionDependency] = None
    """A function that is dependent on a SQL object."""

    table: Optional[TableDependency] = None
    """A table that is dependent on a SQL object."""

    def as_dict(self) -> dict:
        """Serializes the Dependency into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.function: body['function'] = self.function.as_dict()
        if self.table: body['table'] = self.table.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Dependency:
        """Deserializes the Dependency from a dictionary."""
        return cls(function=_from_dict(d, 'function', FunctionDependency),
                   table=_from_dict(d, 'table', TableDependency))


@dataclass
class DependencyList:
    """A list of dependencies."""

    dependencies: Optional[List[Dependency]] = None
    """Array of dependencies."""

    def as_dict(self) -> dict:
        """Serializes the DependencyList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dependencies: body['dependencies'] = [v.as_dict() for v in self.dependencies]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DependencyList:
        """Deserializes the DependencyList from a dictionary."""
        return cls(dependencies=_repeated_dict(d, 'dependencies', Dependency))


@dataclass
class DisableResponse:

    def as_dict(self) -> dict:
        """Serializes the DisableResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DisableResponse:
        """Deserializes the DisableResponse from a dictionary."""
        return cls()


class DisableSchemaName(Enum):

    ACCESS = 'access'
    BILLING = 'billing'
    LINEAGE = 'lineage'
    OPERATIONAL_DATA = 'operational_data'


@dataclass
class EffectivePermissionsList:
    privilege_assignments: Optional[List[EffectivePrivilegeAssignment]] = None
    """The privileges conveyed to each principal (either directly or via inheritance)"""

    def as_dict(self) -> dict:
        """Serializes the EffectivePermissionsList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [v.as_dict() for v in self.privilege_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EffectivePermissionsList:
        """Deserializes the EffectivePermissionsList from a dictionary."""
        return cls(
            privilege_assignments=_repeated_dict(d, 'privilege_assignments', EffectivePrivilegeAssignment))


@dataclass
class EffectivePredictiveOptimizationFlag:
    value: EnablePredictiveOptimization
    """Whether predictive optimization should be enabled for this object and objects under it."""

    inherited_from_name: Optional[str] = None
    """The name of the object from which the flag was inherited. If there was no inheritance, this
    field is left blank."""

    inherited_from_type: Optional[EffectivePredictiveOptimizationFlagInheritedFromType] = None
    """The type of the object from which the flag was inherited. If there was no inheritance, this
    field is left blank."""

    def as_dict(self) -> dict:
        """Serializes the EffectivePredictiveOptimizationFlag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited_from_name is not None: body['inherited_from_name'] = self.inherited_from_name
        if self.inherited_from_type is not None: body['inherited_from_type'] = self.inherited_from_type.value
        if self.value is not None: body['value'] = self.value.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EffectivePredictiveOptimizationFlag:
        """Deserializes the EffectivePredictiveOptimizationFlag from a dictionary."""
        return cls(inherited_from_name=d.get('inherited_from_name', None),
                   inherited_from_type=_enum(d, 'inherited_from_type',
                                             EffectivePredictiveOptimizationFlagInheritedFromType),
                   value=_enum(d, 'value', EnablePredictiveOptimization))


class EffectivePredictiveOptimizationFlagInheritedFromType(Enum):
    """The type of the object from which the flag was inherited. If there was no inheritance, this
    field is left blank."""

    CATALOG = 'CATALOG'
    SCHEMA = 'SCHEMA'


@dataclass
class EffectivePrivilege:
    inherited_from_name: Optional[str] = None
    """The full name of the object that conveys this privilege via inheritance. This field is omitted
    when privilege is not inherited (it's assigned to the securable itself)."""

    inherited_from_type: Optional[SecurableType] = None
    """The type of the object that conveys this privilege via inheritance. This field is omitted when
    privilege is not inherited (it's assigned to the securable itself)."""

    privilege: Optional[Privilege] = None
    """The privilege assigned to the principal."""

    def as_dict(self) -> dict:
        """Serializes the EffectivePrivilege into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited_from_name is not None: body['inherited_from_name'] = self.inherited_from_name
        if self.inherited_from_type is not None: body['inherited_from_type'] = self.inherited_from_type.value
        if self.privilege is not None: body['privilege'] = self.privilege.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EffectivePrivilege:
        """Deserializes the EffectivePrivilege from a dictionary."""
        return cls(inherited_from_name=d.get('inherited_from_name', None),
                   inherited_from_type=_enum(d, 'inherited_from_type', SecurableType),
                   privilege=_enum(d, 'privilege', Privilege))


@dataclass
class EffectivePrivilegeAssignment:
    principal: Optional[str] = None
    """The principal (user email address or group name)."""

    privileges: Optional[List[EffectivePrivilege]] = None
    """The privileges conveyed to the principal (either directly or via inheritance)."""

    def as_dict(self) -> dict:
        """Serializes the EffectivePrivilegeAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.principal is not None: body['principal'] = self.principal
        if self.privileges: body['privileges'] = [v.as_dict() for v in self.privileges]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EffectivePrivilegeAssignment:
        """Deserializes the EffectivePrivilegeAssignment from a dictionary."""
        return cls(principal=d.get('principal', None),
                   privileges=_repeated_dict(d, 'privileges', EffectivePrivilege))


class EnablePredictiveOptimization(Enum):
    """Whether predictive optimization should be enabled for this object and objects under it."""

    DISABLE = 'DISABLE'
    ENABLE = 'ENABLE'
    INHERIT = 'INHERIT'


@dataclass
class EnableResponse:

    def as_dict(self) -> dict:
        """Serializes the EnableResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EnableResponse:
        """Deserializes the EnableResponse from a dictionary."""
        return cls()


class EnableSchemaName(Enum):

    ACCESS = 'access'
    BILLING = 'billing'
    LINEAGE = 'lineage'
    OPERATIONAL_DATA = 'operational_data'


@dataclass
class EncryptionDetails:
    """Encryption options that apply to clients connecting to cloud storage."""

    sse_encryption_details: Optional[SseEncryptionDetails] = None
    """Server-Side Encryption properties for clients communicating with AWS s3."""

    def as_dict(self) -> dict:
        """Serializes the EncryptionDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.sse_encryption_details: body['sse_encryption_details'] = self.sse_encryption_details.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EncryptionDetails:
        """Deserializes the EncryptionDetails from a dictionary."""
        return cls(sse_encryption_details=_from_dict(d, 'sse_encryption_details', SseEncryptionDetails))


@dataclass
class ExternalLocationInfo:
    access_point: Optional[str] = None
    """The AWS access point to use when accesing s3 for this external location."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    created_at: Optional[int] = None
    """Time at which this external location was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of external location creator."""

    credential_id: Optional[str] = None
    """Unique ID of the location's storage credential."""

    credential_name: Optional[str] = None
    """Name of the storage credential used with this location."""

    encryption_details: Optional[EncryptionDetails] = None
    """Encryption options that apply to clients connecting to cloud storage."""

    metastore_id: Optional[str] = None
    """Unique identifier of metastore hosting the external location."""

    name: Optional[str] = None
    """Name of the external location."""

    owner: Optional[str] = None
    """The owner of the external location."""

    read_only: Optional[bool] = None
    """Indicates whether the external location is read-only."""

    updated_at: Optional[int] = None
    """Time at which external location this was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified the external location."""

    url: Optional[str] = None
    """Path URL of the external location."""

    def as_dict(self) -> dict:
        """Serializes the ExternalLocationInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_point is not None: body['access_point'] = self.access_point
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.credential_id is not None: body['credential_id'] = self.credential_id
        if self.credential_name is not None: body['credential_name'] = self.credential_name
        if self.encryption_details: body['encryption_details'] = self.encryption_details.as_dict()
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExternalLocationInfo:
        """Deserializes the ExternalLocationInfo from a dictionary."""
        return cls(access_point=d.get('access_point', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   credential_id=d.get('credential_id', None),
                   credential_name=d.get('credential_name', None),
                   encryption_details=_from_dict(d, 'encryption_details', EncryptionDetails),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   url=d.get('url', None))


@dataclass
class FailedStatus:
    """Detailed status of an online table. Shown if the online table is in the OFFLINE_FAILED or the
    ONLINE_PIPELINE_FAILED state."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the online table. Note that this Delta
    version may only be partially synced to the online table. Only populated if the table is still
    online and available for serving."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the online
    table. Only populated if the table is still online and available for serving."""

    def as_dict(self) -> dict:
        """Serializes the FailedStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_processed_commit_version is not None:
            body['last_processed_commit_version'] = self.last_processed_commit_version
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FailedStatus:
        """Deserializes the FailedStatus from a dictionary."""
        return cls(last_processed_commit_version=d.get('last_processed_commit_version', None),
                   timestamp=d.get('timestamp', None))


@dataclass
class ForeignKeyConstraint:
    name: str
    """The name of the constraint."""

    child_columns: List[str]
    """Column names for this constraint."""

    parent_table: str
    """The full name of the parent constraint."""

    parent_columns: List[str]
    """Column names for this constraint."""

    def as_dict(self) -> dict:
        """Serializes the ForeignKeyConstraint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.child_columns: body['child_columns'] = [v for v in self.child_columns]
        if self.name is not None: body['name'] = self.name
        if self.parent_columns: body['parent_columns'] = [v for v in self.parent_columns]
        if self.parent_table is not None: body['parent_table'] = self.parent_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ForeignKeyConstraint:
        """Deserializes the ForeignKeyConstraint from a dictionary."""
        return cls(child_columns=d.get('child_columns', None),
                   name=d.get('name', None),
                   parent_columns=d.get('parent_columns', None),
                   parent_table=d.get('parent_table', None))


@dataclass
class FunctionDependency:
    """A function that is dependent on a SQL object."""

    function_full_name: str
    """Full name of the dependent function, in the form of
    __catalog_name__.__schema_name__.__function_name__."""

    def as_dict(self) -> dict:
        """Serializes the FunctionDependency into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.function_full_name is not None: body['function_full_name'] = self.function_full_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FunctionDependency:
        """Deserializes the FunctionDependency from a dictionary."""
        return cls(function_full_name=d.get('function_full_name', None))


@dataclass
class FunctionInfo:
    catalog_name: Optional[str] = None
    """Name of parent catalog."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    created_at: Optional[int] = None
    """Time at which this function was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of function creator."""

    data_type: Optional[ColumnTypeName] = None
    """Scalar function return data type."""

    external_language: Optional[str] = None
    """External function language."""

    external_name: Optional[str] = None
    """External function name."""

    full_data_type: Optional[str] = None
    """Pretty printed function data type."""

    full_name: Optional[str] = None
    """Full name of function, in form of __catalog_name__.__schema_name__.__function__name__"""

    function_id: Optional[str] = None
    """Id of Function, relative to parent schema."""

    input_params: Optional[FunctionParameterInfos] = None

    is_deterministic: Optional[bool] = None
    """Whether the function is deterministic."""

    is_null_call: Optional[bool] = None
    """Function null call."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """Name of function, relative to parent schema."""

    owner: Optional[str] = None
    """Username of current owner of function."""

    parameter_style: Optional[FunctionInfoParameterStyle] = None
    """Function parameter style. **S** is the value for SQL."""

    properties: Optional[str] = None
    """JSON-serialized key-value pair map, encoded (escaped) as a string."""

    return_params: Optional[FunctionParameterInfos] = None
    """Table function return parameters."""

    routine_body: Optional[FunctionInfoRoutineBody] = None
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    routine_definition: Optional[str] = None
    """Function body."""

    routine_dependencies: Optional[DependencyList] = None
    """Function dependencies."""

    schema_name: Optional[str] = None
    """Name of parent schema relative to its parent catalog."""

    security_type: Optional[FunctionInfoSecurityType] = None
    """Function security type."""

    specific_name: Optional[str] = None
    """Specific name of the function; Reserved for future use."""

    sql_data_access: Optional[FunctionInfoSqlDataAccess] = None
    """Function SQL data access."""

    sql_path: Optional[str] = None
    """List of schemes whose objects can be referenced without qualification."""

    updated_at: Optional[int] = None
    """Time at which this function was created, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified function."""

    def as_dict(self) -> dict:
        """Serializes the FunctionInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.data_type is not None: body['data_type'] = self.data_type.value
        if self.external_language is not None: body['external_language'] = self.external_language
        if self.external_name is not None: body['external_name'] = self.external_name
        if self.full_data_type is not None: body['full_data_type'] = self.full_data_type
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.function_id is not None: body['function_id'] = self.function_id
        if self.input_params: body['input_params'] = self.input_params.as_dict()
        if self.is_deterministic is not None: body['is_deterministic'] = self.is_deterministic
        if self.is_null_call is not None: body['is_null_call'] = self.is_null_call
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.parameter_style is not None: body['parameter_style'] = self.parameter_style.value
        if self.properties is not None: body['properties'] = self.properties
        if self.return_params: body['return_params'] = self.return_params.as_dict()
        if self.routine_body is not None: body['routine_body'] = self.routine_body.value
        if self.routine_definition is not None: body['routine_definition'] = self.routine_definition
        if self.routine_dependencies: body['routine_dependencies'] = self.routine_dependencies.as_dict()
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.security_type is not None: body['security_type'] = self.security_type.value
        if self.specific_name is not None: body['specific_name'] = self.specific_name
        if self.sql_data_access is not None: body['sql_data_access'] = self.sql_data_access.value
        if self.sql_path is not None: body['sql_path'] = self.sql_path
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FunctionInfo:
        """Deserializes the FunctionInfo from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_type=_enum(d, 'data_type', ColumnTypeName),
                   external_language=d.get('external_language', None),
                   external_name=d.get('external_name', None),
                   full_data_type=d.get('full_data_type', None),
                   full_name=d.get('full_name', None),
                   function_id=d.get('function_id', None),
                   input_params=_from_dict(d, 'input_params', FunctionParameterInfos),
                   is_deterministic=d.get('is_deterministic', None),
                   is_null_call=d.get('is_null_call', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   parameter_style=_enum(d, 'parameter_style', FunctionInfoParameterStyle),
                   properties=d.get('properties', None),
                   return_params=_from_dict(d, 'return_params', FunctionParameterInfos),
                   routine_body=_enum(d, 'routine_body', FunctionInfoRoutineBody),
                   routine_definition=d.get('routine_definition', None),
                   routine_dependencies=_from_dict(d, 'routine_dependencies', DependencyList),
                   schema_name=d.get('schema_name', None),
                   security_type=_enum(d, 'security_type', FunctionInfoSecurityType),
                   specific_name=d.get('specific_name', None),
                   sql_data_access=_enum(d, 'sql_data_access', FunctionInfoSqlDataAccess),
                   sql_path=d.get('sql_path', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class FunctionInfoParameterStyle(Enum):
    """Function parameter style. **S** is the value for SQL."""

    S = 'S'


class FunctionInfoRoutineBody(Enum):
    """Function language. When **EXTERNAL** is used, the language of the routine function should be
    specified in the __external_language__ field, and the __return_params__ of the function cannot
    be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be
    **NO_SQL**."""

    EXTERNAL = 'EXTERNAL'
    SQL = 'SQL'


class FunctionInfoSecurityType(Enum):
    """Function security type."""

    DEFINER = 'DEFINER'


class FunctionInfoSqlDataAccess(Enum):
    """Function SQL data access."""

    CONTAINS_SQL = 'CONTAINS_SQL'
    NO_SQL = 'NO_SQL'
    READS_SQL_DATA = 'READS_SQL_DATA'


@dataclass
class FunctionParameterInfo:
    name: str
    """Name of parameter."""

    type_text: str
    """Full data type spec, SQL/catalogString text."""

    type_name: ColumnTypeName
    """Name of type (INT, STRUCT, MAP, etc.)."""

    position: int
    """Ordinal position of column (starting at position 0)."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    parameter_default: Optional[str] = None
    """Default value of the parameter."""

    parameter_mode: Optional[FunctionParameterMode] = None
    """The mode of the function parameter."""

    parameter_type: Optional[FunctionParameterType] = None
    """The type of function parameter."""

    type_interval_type: Optional[str] = None
    """Format of IntervalType."""

    type_json: Optional[str] = None
    """Full data type spec, JSON-serialized."""

    type_precision: Optional[int] = None
    """Digits of precision; required on Create for DecimalTypes."""

    type_scale: Optional[int] = None
    """Digits to right of decimal; Required on Create for DecimalTypes."""

    def as_dict(self) -> dict:
        """Serializes the FunctionParameterInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.parameter_default is not None: body['parameter_default'] = self.parameter_default
        if self.parameter_mode is not None: body['parameter_mode'] = self.parameter_mode.value
        if self.parameter_type is not None: body['parameter_type'] = self.parameter_type.value
        if self.position is not None: body['position'] = self.position
        if self.type_interval_type is not None: body['type_interval_type'] = self.type_interval_type
        if self.type_json is not None: body['type_json'] = self.type_json
        if self.type_name is not None: body['type_name'] = self.type_name.value
        if self.type_precision is not None: body['type_precision'] = self.type_precision
        if self.type_scale is not None: body['type_scale'] = self.type_scale
        if self.type_text is not None: body['type_text'] = self.type_text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FunctionParameterInfo:
        """Deserializes the FunctionParameterInfo from a dictionary."""
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   parameter_default=d.get('parameter_default', None),
                   parameter_mode=_enum(d, 'parameter_mode', FunctionParameterMode),
                   parameter_type=_enum(d, 'parameter_type', FunctionParameterType),
                   position=d.get('position', None),
                   type_interval_type=d.get('type_interval_type', None),
                   type_json=d.get('type_json', None),
                   type_name=_enum(d, 'type_name', ColumnTypeName),
                   type_precision=d.get('type_precision', None),
                   type_scale=d.get('type_scale', None),
                   type_text=d.get('type_text', None))


@dataclass
class FunctionParameterInfos:
    parameters: Optional[List[FunctionParameterInfo]] = None
    """The array of __FunctionParameterInfo__ definitions of the function's parameters."""

    def as_dict(self) -> dict:
        """Serializes the FunctionParameterInfos into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.parameters: body['parameters'] = [v.as_dict() for v in self.parameters]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FunctionParameterInfos:
        """Deserializes the FunctionParameterInfos from a dictionary."""
        return cls(parameters=_repeated_dict(d, 'parameters', FunctionParameterInfo))


class FunctionParameterMode(Enum):
    """The mode of the function parameter."""

    IN = 'IN'


class FunctionParameterType(Enum):
    """The type of function parameter."""

    COLUMN = 'COLUMN'
    PARAM = 'PARAM'


@dataclass
class GetMetastoreSummaryResponse:
    cloud: Optional[str] = None
    """Cloud vendor of the metastore home shard (e.g., `aws`, `azure`, `gcp`)."""

    created_at: Optional[int] = None
    """Time at which this metastore was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of metastore creator."""

    default_data_access_config_id: Optional[str] = None
    """Unique identifier of the metastore's (Default) Data Access Configuration."""

    delta_sharing_organization_name: Optional[str] = None
    """The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta
    Sharing as the official name."""

    delta_sharing_recipient_token_lifetime_in_seconds: Optional[int] = None
    """The lifetime of delta sharing recipient token in seconds."""

    delta_sharing_scope: Optional[GetMetastoreSummaryResponseDeltaSharingScope] = None
    """The scope of Delta Sharing enabled for the metastore."""

    global_metastore_id: Optional[str] = None
    """Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."""

    metastore_id: Optional[str] = None
    """Unique identifier of metastore."""

    name: Optional[str] = None
    """The user-specified name of the metastore."""

    owner: Optional[str] = None
    """The owner of the metastore."""

    privilege_model_version: Optional[str] = None
    """Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."""

    region: Optional[str] = None
    """Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."""

    storage_root: Optional[str] = None
    """The storage root URL for metastore"""

    storage_root_credential_id: Optional[str] = None
    """UUID of storage credential to access the metastore storage_root."""

    storage_root_credential_name: Optional[str] = None
    """Name of the storage credential to access the metastore storage_root."""

    updated_at: Optional[int] = None
    """Time at which the metastore was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified the metastore."""

    def as_dict(self) -> dict:
        """Serializes the GetMetastoreSummaryResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.default_data_access_config_id is not None:
            body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_organization_name is not None:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds is not None:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope is not None: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.global_metastore_id is not None: body['global_metastore_id'] = self.global_metastore_id
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.privilege_model_version is not None:
            body['privilege_model_version'] = self.privilege_model_version
        if self.region is not None: body['region'] = self.region
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        if self.storage_root_credential_id is not None:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.storage_root_credential_name is not None:
            body['storage_root_credential_name'] = self.storage_root_credential_name
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetMetastoreSummaryResponse:
        """Deserializes the GetMetastoreSummaryResponse from a dictionary."""
        return cls(cloud=d.get('cloud', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   default_data_access_config_id=d.get('default_data_access_config_id', None),
                   delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope',
                                             GetMetastoreSummaryResponseDeltaSharingScope),
                   global_metastore_id=d.get('global_metastore_id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None),
                   storage_root_credential_name=d.get('storage_root_credential_name', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class GetMetastoreSummaryResponseDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


class IsolationMode(Enum):
    """Whether the current securable is accessible from all workspaces or a specific set of workspaces."""

    ISOLATED = 'ISOLATED'
    OPEN = 'OPEN'


@dataclass
class ListAccountMetastoreAssignmentsResponse:
    """The list of workspaces to which the given metastore is assigned."""

    workspace_ids: Optional[List[int]] = None

    def as_dict(self) -> dict:
        """Serializes the ListAccountMetastoreAssignmentsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.workspace_ids: body['workspace_ids'] = [v for v in self.workspace_ids]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListAccountMetastoreAssignmentsResponse:
        """Deserializes the ListAccountMetastoreAssignmentsResponse from a dictionary."""
        return cls(workspace_ids=d.get('workspace_ids', None))


@dataclass
class ListCatalogsResponse:
    catalogs: Optional[List[CatalogInfo]] = None
    """An array of catalog information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListCatalogsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalogs: body['catalogs'] = [v.as_dict() for v in self.catalogs]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListCatalogsResponse:
        """Deserializes the ListCatalogsResponse from a dictionary."""
        return cls(catalogs=_repeated_dict(d, 'catalogs', CatalogInfo))


@dataclass
class ListConnectionsResponse:
    connections: Optional[List[ConnectionInfo]] = None
    """An array of connection information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListConnectionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.connections: body['connections'] = [v.as_dict() for v in self.connections]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListConnectionsResponse:
        """Deserializes the ListConnectionsResponse from a dictionary."""
        return cls(connections=_repeated_dict(d, 'connections', ConnectionInfo))


@dataclass
class ListExternalLocationsResponse:
    external_locations: Optional[List[ExternalLocationInfo]] = None
    """An array of external locations."""

    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    def as_dict(self) -> dict:
        """Serializes the ListExternalLocationsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.external_locations:
            body['external_locations'] = [v.as_dict() for v in self.external_locations]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListExternalLocationsResponse:
        """Deserializes the ListExternalLocationsResponse from a dictionary."""
        return cls(external_locations=_repeated_dict(d, 'external_locations', ExternalLocationInfo),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListFunctionsResponse:
    functions: Optional[List[FunctionInfo]] = None
    """An array of function information objects."""

    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    def as_dict(self) -> dict:
        """Serializes the ListFunctionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.functions: body['functions'] = [v.as_dict() for v in self.functions]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListFunctionsResponse:
        """Deserializes the ListFunctionsResponse from a dictionary."""
        return cls(functions=_repeated_dict(d, 'functions', FunctionInfo),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListMetastoresResponse:
    metastores: Optional[List[MetastoreInfo]] = None
    """An array of metastore information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListMetastoresResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metastores: body['metastores'] = [v.as_dict() for v in self.metastores]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListMetastoresResponse:
        """Deserializes the ListMetastoresResponse from a dictionary."""
        return cls(metastores=_repeated_dict(d, 'metastores', MetastoreInfo))


@dataclass
class ListModelVersionsResponse:
    model_versions: Optional[List[ModelVersionInfo]] = None

    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    def as_dict(self) -> dict:
        """Serializes the ListModelVersionsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.model_versions: body['model_versions'] = [v.as_dict() for v in self.model_versions]
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListModelVersionsResponse:
        """Deserializes the ListModelVersionsResponse from a dictionary."""
        return cls(model_versions=_repeated_dict(d, 'model_versions', ModelVersionInfo),
                   next_page_token=d.get('next_page_token', None))


@dataclass
class ListRegisteredModelsResponse:
    next_page_token: Optional[str] = None
    """Opaque token for pagination. Omitted if there are no more results. page_token should be set to
    this value for fetching the next page."""

    registered_models: Optional[List[RegisteredModelInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListRegisteredModelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.registered_models: body['registered_models'] = [v.as_dict() for v in self.registered_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListRegisteredModelsResponse:
        """Deserializes the ListRegisteredModelsResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   registered_models=_repeated_dict(d, 'registered_models', RegisteredModelInfo))


@dataclass
class ListSchemasResponse:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    schemas: Optional[List[SchemaInfo]] = None
    """An array of schema information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListSchemasResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.schemas: body['schemas'] = [v.as_dict() for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSchemasResponse:
        """Deserializes the ListSchemasResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   schemas=_repeated_dict(d, 'schemas', SchemaInfo))


@dataclass
class ListStorageCredentialsResponse:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    storage_credentials: Optional[List[StorageCredentialInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListStorageCredentialsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.storage_credentials:
            body['storage_credentials'] = [v.as_dict() for v in self.storage_credentials]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListStorageCredentialsResponse:
        """Deserializes the ListStorageCredentialsResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   storage_credentials=_repeated_dict(d, 'storage_credentials', StorageCredentialInfo))


@dataclass
class ListSystemSchemasResponse:
    schemas: Optional[List[SystemSchemaInfo]] = None
    """An array of system schema information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListSystemSchemasResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.schemas: body['schemas'] = [v.as_dict() for v in self.schemas]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListSystemSchemasResponse:
        """Deserializes the ListSystemSchemasResponse from a dictionary."""
        return cls(schemas=_repeated_dict(d, 'schemas', SystemSchemaInfo))


@dataclass
class ListTableSummariesResponse:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    tables: Optional[List[TableSummary]] = None
    """List of table summaries."""

    def as_dict(self) -> dict:
        """Serializes the ListTableSummariesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.tables: body['tables'] = [v.as_dict() for v in self.tables]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListTableSummariesResponse:
        """Deserializes the ListTableSummariesResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   tables=_repeated_dict(d, 'tables', TableSummary))


@dataclass
class ListTablesResponse:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request (for the next page of results)."""

    tables: Optional[List[TableInfo]] = None
    """An array of table information objects."""

    def as_dict(self) -> dict:
        """Serializes the ListTablesResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.tables: body['tables'] = [v.as_dict() for v in self.tables]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListTablesResponse:
        """Deserializes the ListTablesResponse from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   tables=_repeated_dict(d, 'tables', TableInfo))


@dataclass
class ListVolumesResponseContent:
    next_page_token: Optional[str] = None
    """Opaque token to retrieve the next page of results. Absent if there are no more pages.
    __page_token__ should be set to this value for the next request to retrieve the next page of
    results."""

    volumes: Optional[List[VolumeInfo]] = None

    def as_dict(self) -> dict:
        """Serializes the ListVolumesResponseContent into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.next_page_token is not None: body['next_page_token'] = self.next_page_token
        if self.volumes: body['volumes'] = [v.as_dict() for v in self.volumes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListVolumesResponseContent:
        """Deserializes the ListVolumesResponseContent from a dictionary."""
        return cls(next_page_token=d.get('next_page_token', None),
                   volumes=_repeated_dict(d, 'volumes', VolumeInfo))


class MatchType(Enum):
    """The artifact pattern matching type"""

    PREFIX_MATCH = 'PREFIX_MATCH'


@dataclass
class MetastoreAssignment:
    metastore_id: str
    """The unique ID of the metastore."""

    workspace_id: int
    """The unique ID of the Databricks workspace."""

    default_catalog_name: Optional[str] = None
    """The name of the default catalog in the metastore."""

    def as_dict(self) -> dict:
        """Serializes the MetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_catalog_name is not None: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MetastoreAssignment:
        """Deserializes the MetastoreAssignment from a dictionary."""
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


@dataclass
class MetastoreInfo:
    cloud: Optional[str] = None
    """Cloud vendor of the metastore home shard (e.g., `aws`, `azure`, `gcp`)."""

    created_at: Optional[int] = None
    """Time at which this metastore was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of metastore creator."""

    default_data_access_config_id: Optional[str] = None
    """Unique identifier of the metastore's (Default) Data Access Configuration."""

    delta_sharing_organization_name: Optional[str] = None
    """The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta
    Sharing as the official name."""

    delta_sharing_recipient_token_lifetime_in_seconds: Optional[int] = None
    """The lifetime of delta sharing recipient token in seconds."""

    delta_sharing_scope: Optional[MetastoreInfoDeltaSharingScope] = None
    """The scope of Delta Sharing enabled for the metastore."""

    global_metastore_id: Optional[str] = None
    """Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."""

    metastore_id: Optional[str] = None
    """Unique identifier of metastore."""

    name: Optional[str] = None
    """The user-specified name of the metastore."""

    owner: Optional[str] = None
    """The owner of the metastore."""

    privilege_model_version: Optional[str] = None
    """Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."""

    region: Optional[str] = None
    """Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."""

    storage_root: Optional[str] = None
    """The storage root URL for metastore"""

    storage_root_credential_id: Optional[str] = None
    """UUID of storage credential to access the metastore storage_root."""

    storage_root_credential_name: Optional[str] = None
    """Name of the storage credential to access the metastore storage_root."""

    updated_at: Optional[int] = None
    """Time at which the metastore was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified the metastore."""

    def as_dict(self) -> dict:
        """Serializes the MetastoreInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cloud is not None: body['cloud'] = self.cloud
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.default_data_access_config_id is not None:
            body['default_data_access_config_id'] = self.default_data_access_config_id
        if self.delta_sharing_organization_name is not None:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds is not None:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope is not None: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.global_metastore_id is not None: body['global_metastore_id'] = self.global_metastore_id
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.privilege_model_version is not None:
            body['privilege_model_version'] = self.privilege_model_version
        if self.region is not None: body['region'] = self.region
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        if self.storage_root_credential_id is not None:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        if self.storage_root_credential_name is not None:
            body['storage_root_credential_name'] = self.storage_root_credential_name
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MetastoreInfo:
        """Deserializes the MetastoreInfo from a dictionary."""
        return cls(cloud=d.get('cloud', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   default_data_access_config_id=d.get('default_data_access_config_id', None),
                   delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope', MetastoreInfoDeltaSharingScope),
                   global_metastore_id=d.get('global_metastore_id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   region=d.get('region', None),
                   storage_root=d.get('storage_root', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None),
                   storage_root_credential_name=d.get('storage_root_credential_name', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


class MetastoreInfoDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


@dataclass
class ModelVersionInfo:
    catalog_name: Optional[str] = None
    """The name of the catalog containing the model version"""

    comment: Optional[str] = None
    """The comment attached to the model version"""

    created_at: Optional[int] = None

    created_by: Optional[str] = None
    """The identifier of the user who created the model version"""

    id: Optional[str] = None
    """The unique identifier of the model version"""

    metastore_id: Optional[str] = None
    """The unique identifier of the metastore containing the model version"""

    model_name: Optional[str] = None
    """The name of the parent registered model of the model version, relative to parent schema"""

    model_version_dependencies: Optional[DependencyList] = None
    """Model version dependencies, for feature-store packaged models"""

    run_id: Optional[str] = None
    """MLflow run ID used when creating the model version, if ``source`` was generated by an experiment
    run stored in an MLflow tracking server"""

    run_workspace_id: Optional[int] = None
    """ID of the Databricks workspace containing the MLflow run that generated this model version, if
    applicable"""

    schema_name: Optional[str] = None
    """The name of the schema containing the model version, relative to parent catalog"""

    source: Optional[str] = None
    """URI indicating the location of the source artifacts (files) for the model version"""

    status: Optional[ModelVersionInfoStatus] = None
    """Current status of the model version. Newly created model versions start in PENDING_REGISTRATION
    status, then move to READY status once the model version files are uploaded and the model
    version is finalized. Only model versions in READY status can be loaded for inference or served."""

    storage_location: Optional[str] = None
    """The storage location on the cloud under which model version data files are stored"""

    updated_at: Optional[int] = None

    updated_by: Optional[str] = None
    """The identifier of the user who updated the model version last time"""

    version: Optional[int] = None
    """Integer model version number, used to reference the model version in API requests."""

    def as_dict(self) -> dict:
        """Serializes the ModelVersionInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.id is not None: body['id'] = self.id
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version_dependencies:
            body['model_version_dependencies'] = self.model_version_dependencies.as_dict()
        if self.run_id is not None: body['run_id'] = self.run_id
        if self.run_workspace_id is not None: body['run_workspace_id'] = self.run_workspace_id
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.source is not None: body['source'] = self.source
        if self.status is not None: body['status'] = self.status.value
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ModelVersionInfo:
        """Deserializes the ModelVersionInfo from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   id=d.get('id', None),
                   metastore_id=d.get('metastore_id', None),
                   model_name=d.get('model_name', None),
                   model_version_dependencies=_from_dict(d, 'model_version_dependencies', DependencyList),
                   run_id=d.get('run_id', None),
                   run_workspace_id=d.get('run_workspace_id', None),
                   schema_name=d.get('schema_name', None),
                   source=d.get('source', None),
                   status=_enum(d, 'status', ModelVersionInfoStatus),
                   storage_location=d.get('storage_location', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   version=d.get('version', None))


class ModelVersionInfoStatus(Enum):
    """Current status of the model version. Newly created model versions start in PENDING_REGISTRATION
    status, then move to READY status once the model version files are uploaded and the model
    version is finalized. Only model versions in READY status can be loaded for inference or served."""

    FAILED_REGISTRATION = 'FAILED_REGISTRATION'
    PENDING_REGISTRATION = 'PENDING_REGISTRATION'
    READY = 'READY'


@dataclass
class MonitorCronSchedule:
    pause_status: Optional[MonitorCronSchedulePauseStatus] = None
    """Whether the schedule is paused or not"""

    quartz_cron_expression: Optional[str] = None
    """A cron expression using quartz syntax that describes the schedule for a job."""

    timezone_id: Optional[str] = None
    """A Java timezone id. The schedule for a job will be resolved with respect to this timezone."""

    def as_dict(self) -> dict:
        """Serializes the MonitorCronSchedule into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.pause_status is not None: body['pause_status'] = self.pause_status.value
        if self.quartz_cron_expression is not None:
            body['quartz_cron_expression'] = self.quartz_cron_expression
        if self.timezone_id is not None: body['timezone_id'] = self.timezone_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorCronSchedule:
        """Deserializes the MonitorCronSchedule from a dictionary."""
        return cls(pause_status=_enum(d, 'pause_status', MonitorCronSchedulePauseStatus),
                   quartz_cron_expression=d.get('quartz_cron_expression', None),
                   timezone_id=d.get('timezone_id', None))


class MonitorCronSchedulePauseStatus(Enum):
    """Whether the schedule is paused or not"""

    PAUSED = 'PAUSED'
    UNPAUSED = 'UNPAUSED'


@dataclass
class MonitorCustomMetric:
    definition: Optional[str] = None
    """Jinja template for a SQL expression that specifies how to compute the metric. See [create metric
    definition].
    
    [create metric definition]: https://docs.databricks.com/en/lakehouse-monitoring/custom-metrics.html#create-definition"""

    input_columns: Optional[List[str]] = None
    """Columns on the monitored table to apply the custom metrics to."""

    name: Optional[str] = None
    """Name of the custom metric."""

    output_data_type: Optional[str] = None
    """The output type of the custom metric."""

    type: Optional[MonitorCustomMetricType] = None
    """The type of the custom metric."""

    def as_dict(self) -> dict:
        """Serializes the MonitorCustomMetric into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.definition is not None: body['definition'] = self.definition
        if self.input_columns: body['input_columns'] = [v for v in self.input_columns]
        if self.name is not None: body['name'] = self.name
        if self.output_data_type is not None: body['output_data_type'] = self.output_data_type
        if self.type is not None: body['type'] = self.type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorCustomMetric:
        """Deserializes the MonitorCustomMetric from a dictionary."""
        return cls(definition=d.get('definition', None),
                   input_columns=d.get('input_columns', None),
                   name=d.get('name', None),
                   output_data_type=d.get('output_data_type', None),
                   type=_enum(d, 'type', MonitorCustomMetricType))


class MonitorCustomMetricType(Enum):
    """The type of the custom metric."""

    CUSTOM_METRIC_TYPE_AGGREGATE = 'CUSTOM_METRIC_TYPE_AGGREGATE'
    CUSTOM_METRIC_TYPE_DERIVED = 'CUSTOM_METRIC_TYPE_DERIVED'
    CUSTOM_METRIC_TYPE_DRIFT = 'CUSTOM_METRIC_TYPE_DRIFT'
    MONITOR_STATUS_ERROR = 'MONITOR_STATUS_ERROR'
    MONITOR_STATUS_FAILED = 'MONITOR_STATUS_FAILED'


@dataclass
class MonitorDataClassificationConfig:
    enabled: Optional[bool] = None
    """Whether data classification is enabled."""

    def as_dict(self) -> dict:
        """Serializes the MonitorDataClassificationConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorDataClassificationConfig:
        """Deserializes the MonitorDataClassificationConfig from a dictionary."""
        return cls(enabled=d.get('enabled', None))


@dataclass
class MonitorDestinations:
    email_addresses: Optional[List[str]] = None
    """The list of email addresses to send the notification to."""

    def as_dict(self) -> dict:
        """Serializes the MonitorDestinations into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.email_addresses: body['email_addresses'] = [v for v in self.email_addresses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorDestinations:
        """Deserializes the MonitorDestinations from a dictionary."""
        return cls(email_addresses=d.get('email_addresses', None))


@dataclass
class MonitorInferenceLogProfileType:
    granularities: Optional[List[str]] = None
    """List of granularities to use when aggregating data into time windows based on their timestamp."""

    label_col: Optional[str] = None
    """Column of the model label."""

    model_id_col: Optional[str] = None
    """Column of the model id or version."""

    prediction_col: Optional[str] = None
    """Column of the model prediction."""

    prediction_proba_col: Optional[str] = None
    """Column of the model prediction probabilities."""

    problem_type: Optional[MonitorInferenceLogProfileTypeProblemType] = None
    """Problem type the model aims to solve."""

    timestamp_col: Optional[str] = None
    """Column of the timestamp of predictions."""

    def as_dict(self) -> dict:
        """Serializes the MonitorInferenceLogProfileType into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.granularities: body['granularities'] = [v for v in self.granularities]
        if self.label_col is not None: body['label_col'] = self.label_col
        if self.model_id_col is not None: body['model_id_col'] = self.model_id_col
        if self.prediction_col is not None: body['prediction_col'] = self.prediction_col
        if self.prediction_proba_col is not None: body['prediction_proba_col'] = self.prediction_proba_col
        if self.problem_type is not None: body['problem_type'] = self.problem_type.value
        if self.timestamp_col is not None: body['timestamp_col'] = self.timestamp_col
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorInferenceLogProfileType:
        """Deserializes the MonitorInferenceLogProfileType from a dictionary."""
        return cls(granularities=d.get('granularities', None),
                   label_col=d.get('label_col', None),
                   model_id_col=d.get('model_id_col', None),
                   prediction_col=d.get('prediction_col', None),
                   prediction_proba_col=d.get('prediction_proba_col', None),
                   problem_type=_enum(d, 'problem_type', MonitorInferenceLogProfileTypeProblemType),
                   timestamp_col=d.get('timestamp_col', None))


class MonitorInferenceLogProfileTypeProblemType(Enum):
    """Problem type the model aims to solve."""

    PROBLEM_TYPE_CLASSIFICATION = 'PROBLEM_TYPE_CLASSIFICATION'
    PROBLEM_TYPE_REGRESSION = 'PROBLEM_TYPE_REGRESSION'


@dataclass
class MonitorInfo:
    assets_dir: Optional[str] = None
    """The directory to store monitoring assets (e.g. dashboard, metric tables)."""

    baseline_table_name: Optional[str] = None
    """Name of the baseline table from which drift metrics are computed from. Columns in the monitored
    table should also be present in the baseline table."""

    custom_metrics: Optional[List[MonitorCustomMetric]] = None
    """Custom metrics to compute on the monitored table. These can be aggregate metrics, derived
    metrics (from already computed aggregate metrics), or drift metrics (comparing metrics across
    time windows)."""

    dashboard_id: Optional[str] = None
    """The ID of the generated dashboard."""

    data_classification_config: Optional[MonitorDataClassificationConfig] = None
    """The data classification config for the monitor."""

    drift_metrics_table_name: Optional[str] = None
    """The full name of the drift metrics table. Format:
    __catalog_name__.__schema_name__.__table_name__."""

    inference_log: Optional[MonitorInferenceLogProfileType] = None
    """Configuration for monitoring inference logs."""

    latest_monitor_failure_msg: Optional[str] = None
    """The latest failure message of the monitor (if any)."""

    monitor_version: Optional[str] = None
    """The version of the monitor config (e.g. 1,2,3). If negative, the monitor may be corrupted."""

    notifications: Optional[List[MonitorNotificationsConfig]] = None
    """The notification settings for the monitor."""

    output_schema_name: Optional[str] = None
    """Schema where output metric tables are created."""

    profile_metrics_table_name: Optional[str] = None
    """The full name of the profile metrics table. Format:
    __catalog_name__.__schema_name__.__table_name__."""

    schedule: Optional[MonitorCronSchedule] = None
    """The schedule for automatically updating and refreshing metric tables."""

    slicing_exprs: Optional[List[str]] = None
    """List of column expressions to slice data with for targeted analysis. The data is grouped by each
    expression independently, resulting in a separate slice for each predicate and its complements.
    For high-cardinality columns, only the top 100 unique values by frequency will generate slices."""

    snapshot: Optional[MonitorSnapshotProfileType] = None
    """Configuration for monitoring snapshot tables."""

    status: Optional[MonitorInfoStatus] = None
    """The status of the monitor."""

    table_name: Optional[str] = None
    """The full name of the table to monitor. Format: __catalog_name__.__schema_name__.__table_name__."""

    time_series: Optional[MonitorTimeSeriesProfileType] = None
    """Configuration for monitoring time series tables."""

    def as_dict(self) -> dict:
        """Serializes the MonitorInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.assets_dir is not None: body['assets_dir'] = self.assets_dir
        if self.baseline_table_name is not None: body['baseline_table_name'] = self.baseline_table_name
        if self.custom_metrics: body['custom_metrics'] = [v.as_dict() for v in self.custom_metrics]
        if self.dashboard_id is not None: body['dashboard_id'] = self.dashboard_id
        if self.data_classification_config:
            body['data_classification_config'] = self.data_classification_config.as_dict()
        if self.drift_metrics_table_name is not None:
            body['drift_metrics_table_name'] = self.drift_metrics_table_name
        if self.inference_log: body['inference_log'] = self.inference_log.as_dict()
        if self.latest_monitor_failure_msg is not None:
            body['latest_monitor_failure_msg'] = self.latest_monitor_failure_msg
        if self.monitor_version is not None: body['monitor_version'] = self.monitor_version
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.output_schema_name is not None: body['output_schema_name'] = self.output_schema_name
        if self.profile_metrics_table_name is not None:
            body['profile_metrics_table_name'] = self.profile_metrics_table_name
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.slicing_exprs: body['slicing_exprs'] = [v for v in self.slicing_exprs]
        if self.snapshot: body['snapshot'] = self.snapshot.as_dict()
        if self.status is not None: body['status'] = self.status.value
        if self.table_name is not None: body['table_name'] = self.table_name
        if self.time_series: body['time_series'] = self.time_series.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorInfo:
        """Deserializes the MonitorInfo from a dictionary."""
        return cls(assets_dir=d.get('assets_dir', None),
                   baseline_table_name=d.get('baseline_table_name', None),
                   custom_metrics=_repeated_dict(d, 'custom_metrics', MonitorCustomMetric),
                   dashboard_id=d.get('dashboard_id', None),
                   data_classification_config=_from_dict(d, 'data_classification_config',
                                                         MonitorDataClassificationConfig),
                   drift_metrics_table_name=d.get('drift_metrics_table_name', None),
                   inference_log=_from_dict(d, 'inference_log', MonitorInferenceLogProfileType),
                   latest_monitor_failure_msg=d.get('latest_monitor_failure_msg', None),
                   monitor_version=d.get('monitor_version', None),
                   notifications=_repeated_dict(d, 'notifications', MonitorNotificationsConfig),
                   output_schema_name=d.get('output_schema_name', None),
                   profile_metrics_table_name=d.get('profile_metrics_table_name', None),
                   schedule=_from_dict(d, 'schedule', MonitorCronSchedule),
                   slicing_exprs=d.get('slicing_exprs', None),
                   snapshot=_from_dict(d, 'snapshot', MonitorSnapshotProfileType),
                   status=_enum(d, 'status', MonitorInfoStatus),
                   table_name=d.get('table_name', None),
                   time_series=_from_dict(d, 'time_series', MonitorTimeSeriesProfileType))


class MonitorInfoStatus(Enum):
    """The status of the monitor."""

    MONITOR_STATUS_ACTIVE = 'MONITOR_STATUS_ACTIVE'
    MONITOR_STATUS_DELETE_PENDING = 'MONITOR_STATUS_DELETE_PENDING'
    MONITOR_STATUS_ERROR = 'MONITOR_STATUS_ERROR'
    MONITOR_STATUS_FAILED = 'MONITOR_STATUS_FAILED'
    MONITOR_STATUS_PENDING = 'MONITOR_STATUS_PENDING'


@dataclass
class MonitorNotificationsConfig:
    on_failure: Optional[MonitorDestinations] = None
    """Who to send notifications to on monitor failure."""

    def as_dict(self) -> dict:
        """Serializes the MonitorNotificationsConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.on_failure: body['on_failure'] = self.on_failure.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorNotificationsConfig:
        """Deserializes the MonitorNotificationsConfig from a dictionary."""
        return cls(on_failure=_from_dict(d, 'on_failure', MonitorDestinations))


@dataclass
class MonitorRefreshInfo:
    end_time_ms: Optional[int] = None
    """The time at which the refresh ended, in epoch milliseconds."""

    message: Optional[str] = None
    """An optional message to give insight into the current state of the job (e.g. FAILURE messages)."""

    refresh_id: Optional[int] = None
    """The ID of the refresh."""

    start_time_ms: Optional[int] = None
    """The time at which the refresh started, in epoch milliseconds."""

    state: Optional[MonitorRefreshInfoState] = None
    """The current state of the refresh."""

    def as_dict(self) -> dict:
        """Serializes the MonitorRefreshInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.end_time_ms is not None: body['end_time_ms'] = self.end_time_ms
        if self.message is not None: body['message'] = self.message
        if self.refresh_id is not None: body['refresh_id'] = self.refresh_id
        if self.start_time_ms is not None: body['start_time_ms'] = self.start_time_ms
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorRefreshInfo:
        """Deserializes the MonitorRefreshInfo from a dictionary."""
        return cls(end_time_ms=d.get('end_time_ms', None),
                   message=d.get('message', None),
                   refresh_id=d.get('refresh_id', None),
                   start_time_ms=d.get('start_time_ms', None),
                   state=_enum(d, 'state', MonitorRefreshInfoState))


class MonitorRefreshInfoState(Enum):
    """The current state of the refresh."""

    CANCELED = 'CANCELED'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'


@dataclass
class MonitorSnapshotProfileType:

    def as_dict(self) -> dict:
        """Serializes the MonitorSnapshotProfileType into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorSnapshotProfileType:
        """Deserializes the MonitorSnapshotProfileType from a dictionary."""
        return cls()


@dataclass
class MonitorTimeSeriesProfileType:
    granularities: Optional[List[str]] = None
    """List of granularities to use when aggregating data into time windows based on their timestamp."""

    timestamp_col: Optional[str] = None
    """The timestamp column. This must be timestamp types or convertible to timestamp types using the
    pyspark to_timestamp function."""

    def as_dict(self) -> dict:
        """Serializes the MonitorTimeSeriesProfileType into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.granularities: body['granularities'] = [v for v in self.granularities]
        if self.timestamp_col is not None: body['timestamp_col'] = self.timestamp_col
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> MonitorTimeSeriesProfileType:
        """Deserializes the MonitorTimeSeriesProfileType from a dictionary."""
        return cls(granularities=d.get('granularities', None), timestamp_col=d.get('timestamp_col', None))


@dataclass
class NamedTableConstraint:
    name: str
    """The name of the constraint."""

    def as_dict(self) -> dict:
        """Serializes the NamedTableConstraint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> NamedTableConstraint:
        """Deserializes the NamedTableConstraint from a dictionary."""
        return cls(name=d.get('name', None))


@dataclass
class OnlineTable:
    """Online Table information."""

    name: Optional[str] = None
    """Full three-part (catalog, schema, table) name of the table."""

    spec: Optional[OnlineTableSpec] = None
    """Specification of the online table."""

    status: Optional[OnlineTableStatus] = None
    """Online Table status"""

    def as_dict(self) -> dict:
        """Serializes the OnlineTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.spec: body['spec'] = self.spec.as_dict()
        if self.status: body['status'] = self.status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OnlineTable:
        """Deserializes the OnlineTable from a dictionary."""
        return cls(name=d.get('name', None),
                   spec=_from_dict(d, 'spec', OnlineTableSpec),
                   status=_from_dict(d, 'status', OnlineTableStatus))


@dataclass
class OnlineTableSpec:
    """Specification of an online table."""

    perform_full_copy: Optional[bool] = None
    """Whether to create a full-copy pipeline -- a pipeline that stops after creates a full copy of the
    source table upon initialization and does not process any change data feeds (CDFs) afterwards.
    The pipeline can still be manually triggered afterwards, but it always perform a full copy of
    the source table and there are no incremental updates. This mode is useful for syncing views or
    tables without CDFs to online tables. Note that the full-copy pipeline only supports "triggered"
    scheduling policy."""

    pipeline_id: Optional[str] = None
    """ID of the associated pipeline. Generated by the server - cannot be set by the caller."""

    primary_key_columns: Optional[List[str]] = None
    """Primary Key columns to be used for data insert/update in the destination."""

    run_continuously: Optional[OnlineTableSpecContinuousSchedulingPolicy] = None
    """Pipeline runs continuously after generating the initial data."""

    run_triggered: Optional[OnlineTableSpecTriggeredSchedulingPolicy] = None
    """Pipeline stops after generating the initial data and can be triggered later (manually, through a
    cron job or through data triggers)"""

    source_table_full_name: Optional[str] = None
    """Three-part (catalog, schema, table) name of the source Delta table."""

    timeseries_key: Optional[str] = None
    """Time series key to deduplicate (tie-break) rows with the same primary key."""

    def as_dict(self) -> dict:
        """Serializes the OnlineTableSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.perform_full_copy is not None: body['perform_full_copy'] = self.perform_full_copy
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.primary_key_columns: body['primary_key_columns'] = [v for v in self.primary_key_columns]
        if self.run_continuously: body['run_continuously'] = self.run_continuously.as_dict()
        if self.run_triggered: body['run_triggered'] = self.run_triggered.as_dict()
        if self.source_table_full_name is not None:
            body['source_table_full_name'] = self.source_table_full_name
        if self.timeseries_key is not None: body['timeseries_key'] = self.timeseries_key
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OnlineTableSpec:
        """Deserializes the OnlineTableSpec from a dictionary."""
        return cls(perform_full_copy=d.get('perform_full_copy', None),
                   pipeline_id=d.get('pipeline_id', None),
                   primary_key_columns=d.get('primary_key_columns', None),
                   run_continuously=_from_dict(d, 'run_continuously',
                                               OnlineTableSpecContinuousSchedulingPolicy),
                   run_triggered=_from_dict(d, 'run_triggered', OnlineTableSpecTriggeredSchedulingPolicy),
                   source_table_full_name=d.get('source_table_full_name', None),
                   timeseries_key=d.get('timeseries_key', None))


@dataclass
class OnlineTableSpecContinuousSchedulingPolicy:

    def as_dict(self) -> dict:
        """Serializes the OnlineTableSpecContinuousSchedulingPolicy into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OnlineTableSpecContinuousSchedulingPolicy:
        """Deserializes the OnlineTableSpecContinuousSchedulingPolicy from a dictionary."""
        return cls()


@dataclass
class OnlineTableSpecTriggeredSchedulingPolicy:

    def as_dict(self) -> dict:
        """Serializes the OnlineTableSpecTriggeredSchedulingPolicy into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OnlineTableSpecTriggeredSchedulingPolicy:
        """Deserializes the OnlineTableSpecTriggeredSchedulingPolicy from a dictionary."""
        return cls()


class OnlineTableState(Enum):
    """The state of an online table."""

    OFFLINE = 'OFFLINE'
    OFFLINE_FAILED = 'OFFLINE_FAILED'
    ONLINE = 'ONLINE'
    ONLINE_CONTINUOUS_UPDATE = 'ONLINE_CONTINUOUS_UPDATE'
    ONLINE_NO_PENDING_UPDATE = 'ONLINE_NO_PENDING_UPDATE'
    ONLINE_PIPELINE_FAILED = 'ONLINE_PIPELINE_FAILED'
    ONLINE_TABLE_STATE_UNSPECIFIED = 'ONLINE_TABLE_STATE_UNSPECIFIED'
    ONLINE_TRIGGERED_UPDATE = 'ONLINE_TRIGGERED_UPDATE'
    ONLINE_UPDATING_PIPELINE_RESOURCES = 'ONLINE_UPDATING_PIPELINE_RESOURCES'
    PROVISIONING = 'PROVISIONING'
    PROVISIONING_INITIAL_SNAPSHOT = 'PROVISIONING_INITIAL_SNAPSHOT'
    PROVISIONING_PIPELINE_RESOURCES = 'PROVISIONING_PIPELINE_RESOURCES'


@dataclass
class OnlineTableStatus:
    """Status of an online table."""

    continuous_update_status: Optional[ContinuousUpdateStatus] = None
    """Detailed status of an online table. Shown if the online table is in the ONLINE_CONTINUOUS_UPDATE
    or the ONLINE_UPDATING_PIPELINE_RESOURCES state."""

    detailed_state: Optional[OnlineTableState] = None
    """The state of the online table."""

    failed_status: Optional[FailedStatus] = None
    """Detailed status of an online table. Shown if the online table is in the OFFLINE_FAILED or the
    ONLINE_PIPELINE_FAILED state."""

    message: Optional[str] = None
    """A text description of the current state of the online table."""

    provisioning_status: Optional[ProvisioningStatus] = None
    """Detailed status of an online table. Shown if the online table is in the
    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state."""

    triggered_update_status: Optional[TriggeredUpdateStatus] = None
    """Detailed status of an online table. Shown if the online table is in the ONLINE_TRIGGERED_UPDATE
    or the ONLINE_NO_PENDING_UPDATE state."""

    def as_dict(self) -> dict:
        """Serializes the OnlineTableStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.continuous_update_status:
            body['continuous_update_status'] = self.continuous_update_status.as_dict()
        if self.detailed_state is not None: body['detailed_state'] = self.detailed_state.value
        if self.failed_status: body['failed_status'] = self.failed_status.as_dict()
        if self.message is not None: body['message'] = self.message
        if self.provisioning_status: body['provisioning_status'] = self.provisioning_status.as_dict()
        if self.triggered_update_status:
            body['triggered_update_status'] = self.triggered_update_status.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OnlineTableStatus:
        """Deserializes the OnlineTableStatus from a dictionary."""
        return cls(continuous_update_status=_from_dict(d, 'continuous_update_status', ContinuousUpdateStatus),
                   detailed_state=_enum(d, 'detailed_state', OnlineTableState),
                   failed_status=_from_dict(d, 'failed_status', FailedStatus),
                   message=d.get('message', None),
                   provisioning_status=_from_dict(d, 'provisioning_status', ProvisioningStatus),
                   triggered_update_status=_from_dict(d, 'triggered_update_status', TriggeredUpdateStatus))


@dataclass
class PermissionsChange:
    add: Optional[List[Privilege]] = None
    """The set of privileges to add."""

    principal: Optional[str] = None
    """The principal whose privileges we are changing."""

    remove: Optional[List[Privilege]] = None
    """The set of privileges to remove."""

    def as_dict(self) -> dict:
        """Serializes the PermissionsChange into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.add: body['add'] = [v.value for v in self.add]
        if self.principal is not None: body['principal'] = self.principal
        if self.remove: body['remove'] = [v.value for v in self.remove]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionsChange:
        """Deserializes the PermissionsChange from a dictionary."""
        return cls(add=_repeated_enum(d, 'add', Privilege),
                   principal=d.get('principal', None),
                   remove=_repeated_enum(d, 'remove', Privilege))


@dataclass
class PermissionsList:
    privilege_assignments: Optional[List[PrivilegeAssignment]] = None
    """The privileges assigned to each principal"""

    def as_dict(self) -> dict:
        """Serializes the PermissionsList into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.privilege_assignments:
            body['privilege_assignments'] = [v.as_dict() for v in self.privilege_assignments]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PermissionsList:
        """Deserializes the PermissionsList from a dictionary."""
        return cls(privilege_assignments=_repeated_dict(d, 'privilege_assignments', PrivilegeAssignment))


@dataclass
class PipelineProgress:
    """Progress information of the Online Table data synchronization pipeline."""

    estimated_completion_time_seconds: Optional[float] = None
    """The estimated time remaining to complete this update in seconds."""

    latest_version_currently_processing: Optional[int] = None
    """The source table Delta version that was last processed by the pipeline. The pipeline may not
    have completely processed this version yet."""

    sync_progress_completion: Optional[float] = None
    """The completion ratio of this update. This is a number between 0 and 1."""

    synced_row_count: Optional[int] = None
    """The number of rows that have been synced in this update."""

    total_row_count: Optional[int] = None
    """The total number of rows that need to be synced in this update. This number may be an estimate."""

    def as_dict(self) -> dict:
        """Serializes the PipelineProgress into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.estimated_completion_time_seconds is not None:
            body['estimated_completion_time_seconds'] = self.estimated_completion_time_seconds
        if self.latest_version_currently_processing is not None:
            body['latest_version_currently_processing'] = self.latest_version_currently_processing
        if self.sync_progress_completion is not None:
            body['sync_progress_completion'] = self.sync_progress_completion
        if self.synced_row_count is not None: body['synced_row_count'] = self.synced_row_count
        if self.total_row_count is not None: body['total_row_count'] = self.total_row_count
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PipelineProgress:
        """Deserializes the PipelineProgress from a dictionary."""
        return cls(estimated_completion_time_seconds=d.get('estimated_completion_time_seconds', None),
                   latest_version_currently_processing=d.get('latest_version_currently_processing', None),
                   sync_progress_completion=d.get('sync_progress_completion', None),
                   synced_row_count=d.get('synced_row_count', None),
                   total_row_count=d.get('total_row_count', None))


@dataclass
class PrimaryKeyConstraint:
    name: str
    """The name of the constraint."""

    child_columns: List[str]
    """Column names for this constraint."""

    def as_dict(self) -> dict:
        """Serializes the PrimaryKeyConstraint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.child_columns: body['child_columns'] = [v for v in self.child_columns]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PrimaryKeyConstraint:
        """Deserializes the PrimaryKeyConstraint from a dictionary."""
        return cls(child_columns=d.get('child_columns', None), name=d.get('name', None))


class Privilege(Enum):

    ALL_PRIVILEGES = 'ALL_PRIVILEGES'
    APPLY_TAG = 'APPLY_TAG'
    CREATE = 'CREATE'
    CREATE_CATALOG = 'CREATE_CATALOG'
    CREATE_CONNECTION = 'CREATE_CONNECTION'
    CREATE_EXTERNAL_LOCATION = 'CREATE_EXTERNAL_LOCATION'
    CREATE_EXTERNAL_TABLE = 'CREATE_EXTERNAL_TABLE'
    CREATE_EXTERNAL_VOLUME = 'CREATE_EXTERNAL_VOLUME'
    CREATE_FOREIGN_CATALOG = 'CREATE_FOREIGN_CATALOG'
    CREATE_FUNCTION = 'CREATE_FUNCTION'
    CREATE_MANAGED_STORAGE = 'CREATE_MANAGED_STORAGE'
    CREATE_MATERIALIZED_VIEW = 'CREATE_MATERIALIZED_VIEW'
    CREATE_MODEL = 'CREATE_MODEL'
    CREATE_PROVIDER = 'CREATE_PROVIDER'
    CREATE_RECIPIENT = 'CREATE_RECIPIENT'
    CREATE_SCHEMA = 'CREATE_SCHEMA'
    CREATE_SHARE = 'CREATE_SHARE'
    CREATE_STORAGE_CREDENTIAL = 'CREATE_STORAGE_CREDENTIAL'
    CREATE_TABLE = 'CREATE_TABLE'
    CREATE_VIEW = 'CREATE_VIEW'
    CREATE_VOLUME = 'CREATE_VOLUME'
    EXECUTE = 'EXECUTE'
    MANAGE_ALLOWLIST = 'MANAGE_ALLOWLIST'
    MODIFY = 'MODIFY'
    READ_FILES = 'READ_FILES'
    READ_PRIVATE_FILES = 'READ_PRIVATE_FILES'
    READ_VOLUME = 'READ_VOLUME'
    REFRESH = 'REFRESH'
    SELECT = 'SELECT'
    SET_SHARE_PERMISSION = 'SET_SHARE_PERMISSION'
    USAGE = 'USAGE'
    USE_CATALOG = 'USE_CATALOG'
    USE_CONNECTION = 'USE_CONNECTION'
    USE_MARKETPLACE_ASSETS = 'USE_MARKETPLACE_ASSETS'
    USE_PROVIDER = 'USE_PROVIDER'
    USE_RECIPIENT = 'USE_RECIPIENT'
    USE_SCHEMA = 'USE_SCHEMA'
    USE_SHARE = 'USE_SHARE'
    WRITE_FILES = 'WRITE_FILES'
    WRITE_PRIVATE_FILES = 'WRITE_PRIVATE_FILES'
    WRITE_VOLUME = 'WRITE_VOLUME'


@dataclass
class PrivilegeAssignment:
    principal: Optional[str] = None
    """The principal (user email address or group name)."""

    privileges: Optional[List[Privilege]] = None
    """The privileges assigned to the principal."""

    def as_dict(self) -> dict:
        """Serializes the PrivilegeAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.principal is not None: body['principal'] = self.principal
        if self.privileges: body['privileges'] = [v.value for v in self.privileges]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PrivilegeAssignment:
        """Deserializes the PrivilegeAssignment from a dictionary."""
        return cls(principal=d.get('principal', None), privileges=_repeated_enum(d, 'privileges', Privilege))


PropertiesKvPairs = Dict[str, str]


@dataclass
class ProvisioningInfo:
    """Status of an asynchronously provisioned resource."""

    state: Optional[ProvisioningInfoState] = None

    def as_dict(self) -> dict:
        """Serializes the ProvisioningInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ProvisioningInfo:
        """Deserializes the ProvisioningInfo from a dictionary."""
        return cls(state=_enum(d, 'state', ProvisioningInfoState))


class ProvisioningInfoState(Enum):

    ACTIVE = 'ACTIVE'
    DELETING = 'DELETING'
    FAILED = 'FAILED'
    PROVISIONING = 'PROVISIONING'
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'


@dataclass
class ProvisioningStatus:
    """Detailed status of an online table. Shown if the online table is in the
    PROVISIONING_PIPELINE_RESOURCES or the PROVISIONING_INITIAL_SNAPSHOT state."""

    initial_pipeline_sync_progress: Optional[PipelineProgress] = None
    """Details about initial data synchronization. Only populated when in the
    PROVISIONING_INITIAL_SNAPSHOT state."""

    def as_dict(self) -> dict:
        """Serializes the ProvisioningStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.initial_pipeline_sync_progress:
            body['initial_pipeline_sync_progress'] = self.initial_pipeline_sync_progress.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ProvisioningStatus:
        """Deserializes the ProvisioningStatus from a dictionary."""
        return cls(
            initial_pipeline_sync_progress=_from_dict(d, 'initial_pipeline_sync_progress', PipelineProgress))


@dataclass
class RegisteredModelAlias:
    """Registered model alias."""

    alias_name: Optional[str] = None
    """Name of the alias, e.g. 'champion' or 'latest_stable'"""

    version_num: Optional[int] = None
    """Integer version number of the model version to which this alias points."""

    def as_dict(self) -> dict:
        """Serializes the RegisteredModelAlias into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alias_name is not None: body['alias_name'] = self.alias_name
        if self.version_num is not None: body['version_num'] = self.version_num
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RegisteredModelAlias:
        """Deserializes the RegisteredModelAlias from a dictionary."""
        return cls(alias_name=d.get('alias_name', None), version_num=d.get('version_num', None))


@dataclass
class RegisteredModelInfo:
    aliases: Optional[List[RegisteredModelAlias]] = None
    """List of aliases associated with the registered model"""

    catalog_name: Optional[str] = None
    """The name of the catalog where the schema and the registered model reside"""

    comment: Optional[str] = None
    """The comment attached to the registered model"""

    created_at: Optional[int] = None
    """Creation timestamp of the registered model in milliseconds since the Unix epoch"""

    created_by: Optional[str] = None
    """The identifier of the user who created the registered model"""

    full_name: Optional[str] = None
    """The three-level (fully qualified) name of the registered model"""

    metastore_id: Optional[str] = None
    """The unique identifier of the metastore"""

    name: Optional[str] = None
    """The name of the registered model"""

    owner: Optional[str] = None
    """The identifier of the user who owns the registered model"""

    schema_name: Optional[str] = None
    """The name of the schema where the registered model resides"""

    storage_location: Optional[str] = None
    """The storage location on the cloud under which model version data files are stored"""

    updated_at: Optional[int] = None
    """Last-update timestamp of the registered model in milliseconds since the Unix epoch"""

    updated_by: Optional[str] = None
    """The identifier of the user who updated the registered model last time"""

    def as_dict(self) -> dict:
        """Serializes the RegisteredModelInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aliases: body['aliases'] = [v.as_dict() for v in self.aliases]
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RegisteredModelInfo:
        """Deserializes the RegisteredModelInfo from a dictionary."""
        return cls(aliases=_repeated_dict(d, 'aliases', RegisteredModelAlias),
                   catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   schema_name=d.get('schema_name', None),
                   storage_location=d.get('storage_location', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


@dataclass
class SchemaInfo:
    catalog_name: Optional[str] = None
    """Name of parent catalog."""

    catalog_type: Optional[str] = None
    """The type of the parent catalog."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    created_at: Optional[int] = None
    """Time at which this schema was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of schema creator."""

    effective_predictive_optimization_flag: Optional[EffectivePredictiveOptimizationFlag] = None

    enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None
    """Whether predictive optimization should be enabled for this object and objects under it."""

    full_name: Optional[str] = None
    """Full name of schema, in form of __catalog_name__.__schema_name__."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """Name of schema, relative to parent catalog."""

    owner: Optional[str] = None
    """Username of current owner of schema."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    storage_location: Optional[str] = None
    """Storage location for managed tables within schema."""

    storage_root: Optional[str] = None
    """Storage root URL for managed tables within schema."""

    updated_at: Optional[int] = None
    """Time at which this schema was created, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified schema."""

    def as_dict(self) -> dict:
        """Serializes the SchemaInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.catalog_type is not None: body['catalog_type'] = self.catalog_type
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.effective_predictive_optimization_flag:
            body[
                'effective_predictive_optimization_flag'] = self.effective_predictive_optimization_flag.as_dict(
                )
        if self.enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = self.enable_predictive_optimization.value
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.storage_root is not None: body['storage_root'] = self.storage_root
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SchemaInfo:
        """Deserializes the SchemaInfo from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   catalog_type=d.get('catalog_type', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   effective_predictive_optimization_flag=_from_dict(
                       d, 'effective_predictive_optimization_flag', EffectivePredictiveOptimizationFlag),
                   enable_predictive_optimization=_enum(d, 'enable_predictive_optimization',
                                                        EnablePredictiveOptimization),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None),
                   storage_location=d.get('storage_location', None),
                   storage_root=d.get('storage_root', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None))


SecurableOptionsMap = Dict[str, str]

SecurablePropertiesMap = Dict[str, str]


class SecurableType(Enum):
    """The type of Unity Catalog securable"""

    CATALOG = 'catalog'
    CONNECTION = 'connection'
    EXTERNAL_LOCATION = 'external_location'
    FUNCTION = 'function'
    METASTORE = 'metastore'
    PIPELINE = 'pipeline'
    PROVIDER = 'provider'
    RECIPIENT = 'recipient'
    SCHEMA = 'schema'
    SHARE = 'share'
    STORAGE_CREDENTIAL = 'storage_credential'
    TABLE = 'table'
    VOLUME = 'volume'


@dataclass
class SetArtifactAllowlist:
    artifact_matchers: List[ArtifactMatcher]
    """A list of allowed artifact match patterns."""

    artifact_type: Optional[ArtifactType] = None
    """The artifact type of the allowlist."""

    def as_dict(self) -> dict:
        """Serializes the SetArtifactAllowlist into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.artifact_matchers: body['artifact_matchers'] = [v.as_dict() for v in self.artifact_matchers]
        if self.artifact_type is not None: body['artifact_type'] = self.artifact_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SetArtifactAllowlist:
        """Deserializes the SetArtifactAllowlist from a dictionary."""
        return cls(artifact_matchers=_repeated_dict(d, 'artifact_matchers', ArtifactMatcher),
                   artifact_type=_enum(d, 'artifact_type', ArtifactType))


@dataclass
class SetRegisteredModelAliasRequest:
    full_name: str
    """Full name of the registered model"""

    alias: str
    """The name of the alias"""

    version_num: int
    """The version number of the model version to which the alias points"""

    def as_dict(self) -> dict:
        """Serializes the SetRegisteredModelAliasRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.alias is not None: body['alias'] = self.alias
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.version_num is not None: body['version_num'] = self.version_num
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SetRegisteredModelAliasRequest:
        """Deserializes the SetRegisteredModelAliasRequest from a dictionary."""
        return cls(alias=d.get('alias', None),
                   full_name=d.get('full_name', None),
                   version_num=d.get('version_num', None))


@dataclass
class SseEncryptionDetails:
    """Server-Side Encryption properties for clients communicating with AWS s3."""

    algorithm: Optional[SseEncryptionDetailsAlgorithm] = None
    """The type of key encryption to use (affects headers from s3 client)."""

    aws_kms_key_arn: Optional[str] = None
    """When algorithm is **AWS_SSE_KMS** this field specifies the ARN of the SSE key to use."""

    def as_dict(self) -> dict:
        """Serializes the SseEncryptionDetails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.algorithm is not None: body['algorithm'] = self.algorithm.value
        if self.aws_kms_key_arn is not None: body['aws_kms_key_arn'] = self.aws_kms_key_arn
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SseEncryptionDetails:
        """Deserializes the SseEncryptionDetails from a dictionary."""
        return cls(algorithm=_enum(d, 'algorithm', SseEncryptionDetailsAlgorithm),
                   aws_kms_key_arn=d.get('aws_kms_key_arn', None))


class SseEncryptionDetailsAlgorithm(Enum):
    """The type of key encryption to use (affects headers from s3 client)."""

    AWS_SSE_KMS = 'AWS_SSE_KMS'
    AWS_SSE_S3 = 'AWS_SSE_S3'


@dataclass
class StorageCredentialInfo:
    aws_iam_role: Optional[AwsIamRole] = None
    """The AWS IAM role configuration."""

    azure_managed_identity: Optional[AzureManagedIdentity] = None
    """The Azure managed identity configuration."""

    azure_service_principal: Optional[AzureServicePrincipal] = None
    """The Azure service principal configuration."""

    cloudflare_api_token: Optional[CloudflareApiToken] = None
    """The Cloudflare API token configuration."""

    comment: Optional[str] = None
    """Comment associated with the credential."""

    created_at: Optional[int] = None
    """Time at which this Credential was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of credential creator."""

    databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountResponse] = None
    """The <Databricks> managed GCP service account configuration."""

    id: Optional[str] = None
    """The unique identifier of the credential."""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """The credential name. The name must be unique within the metastore."""

    owner: Optional[str] = None
    """Username of current owner of credential."""

    read_only: Optional[bool] = None
    """Whether the storage credential is only usable for read operations."""

    updated_at: Optional[int] = None
    """Time at which this credential was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified the credential."""

    used_for_managed_storage: Optional[bool] = None
    """Whether this credential is the current metastore's root storage credential."""

    def as_dict(self) -> dict:
        """Serializes the StorageCredentialInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_managed_identity: body['azure_managed_identity'] = self.azure_managed_identity.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.cloudflare_api_token: body['cloudflare_api_token'] = self.cloudflare_api_token.as_dict()
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.databricks_gcp_service_account:
            body['databricks_gcp_service_account'] = self.databricks_gcp_service_account.as_dict()
        if self.id is not None: body['id'] = self.id
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.used_for_managed_storage is not None:
            body['used_for_managed_storage'] = self.used_for_managed_storage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> StorageCredentialInfo:
        """Deserializes the StorageCredentialInfo from a dictionary."""
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_managed_identity=_from_dict(d, 'azure_managed_identity', AzureManagedIdentity),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   cloudflare_api_token=_from_dict(d, 'cloudflare_api_token', CloudflareApiToken),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   databricks_gcp_service_account=_from_dict(d, 'databricks_gcp_service_account',
                                                             DatabricksGcpServiceAccountResponse),
                   id=d.get('id', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   used_for_managed_storage=d.get('used_for_managed_storage', None))


@dataclass
class SystemSchemaInfo:
    schema: Optional[str] = None
    """Name of the system schema."""

    state: Optional[SystemSchemaInfoState] = None
    """The current state of enablement for the system schema. An empty string means the system schema
    is available and ready for opt-in."""

    def as_dict(self) -> dict:
        """Serializes the SystemSchemaInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.schema is not None: body['schema'] = self.schema
        if self.state is not None: body['state'] = self.state.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> SystemSchemaInfo:
        """Deserializes the SystemSchemaInfo from a dictionary."""
        return cls(schema=d.get('schema', None), state=_enum(d, 'state', SystemSchemaInfoState))


class SystemSchemaInfoState(Enum):
    """The current state of enablement for the system schema. An empty string means the system schema
    is available and ready for opt-in."""

    AVAILABLE = 'AVAILABLE'
    DISABLE_INITIALIZED = 'DISABLE_INITIALIZED'
    ENABLE_COMPLETED = 'ENABLE_COMPLETED'
    ENABLE_INITIALIZED = 'ENABLE_INITIALIZED'
    UNAVAILABLE = 'UNAVAILABLE'


@dataclass
class TableConstraint:
    """A table constraint, as defined by *one* of the following fields being set:
    __primary_key_constraint__, __foreign_key_constraint__, __named_table_constraint__."""

    foreign_key_constraint: Optional[ForeignKeyConstraint] = None

    named_table_constraint: Optional[NamedTableConstraint] = None

    primary_key_constraint: Optional[PrimaryKeyConstraint] = None

    def as_dict(self) -> dict:
        """Serializes the TableConstraint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.foreign_key_constraint: body['foreign_key_constraint'] = self.foreign_key_constraint.as_dict()
        if self.named_table_constraint: body['named_table_constraint'] = self.named_table_constraint.as_dict()
        if self.primary_key_constraint: body['primary_key_constraint'] = self.primary_key_constraint.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableConstraint:
        """Deserializes the TableConstraint from a dictionary."""
        return cls(foreign_key_constraint=_from_dict(d, 'foreign_key_constraint', ForeignKeyConstraint),
                   named_table_constraint=_from_dict(d, 'named_table_constraint', NamedTableConstraint),
                   primary_key_constraint=_from_dict(d, 'primary_key_constraint', PrimaryKeyConstraint))


@dataclass
class TableDependency:
    """A table that is dependent on a SQL object."""

    table_full_name: str
    """Full name of the dependent table, in the form of
    __catalog_name__.__schema_name__.__table_name__."""

    def as_dict(self) -> dict:
        """Serializes the TableDependency into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.table_full_name is not None: body['table_full_name'] = self.table_full_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableDependency:
        """Deserializes the TableDependency from a dictionary."""
        return cls(table_full_name=d.get('table_full_name', None))


@dataclass
class TableExistsResponse:
    table_exists: Optional[bool] = None
    """Whether the table exists or not."""

    def as_dict(self) -> dict:
        """Serializes the TableExistsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.table_exists is not None: body['table_exists'] = self.table_exists
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableExistsResponse:
        """Deserializes the TableExistsResponse from a dictionary."""
        return cls(table_exists=d.get('table_exists', None))


@dataclass
class TableInfo:
    access_point: Optional[str] = None
    """The AWS access point to use when accesing s3 for this external location."""

    catalog_name: Optional[str] = None
    """Name of parent catalog."""

    columns: Optional[List[ColumnInfo]] = None
    """The array of __ColumnInfo__ definitions of the table's columns."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    created_at: Optional[int] = None
    """Time at which this table was created, in epoch milliseconds."""

    created_by: Optional[str] = None
    """Username of table creator."""

    data_access_configuration_id: Optional[str] = None
    """Unique ID of the Data Access Configuration to use with the table data."""

    data_source_format: Optional[DataSourceFormat] = None
    """Data source format"""

    deleted_at: Optional[int] = None
    """Time at which this table was deleted, in epoch milliseconds. Field is omitted if table is not
    deleted."""

    delta_runtime_properties_kvpairs: Optional[DeltaRuntimePropertiesKvPairs] = None
    """Information pertaining to current state of the delta table."""

    effective_predictive_optimization_flag: Optional[EffectivePredictiveOptimizationFlag] = None

    enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None
    """Whether predictive optimization should be enabled for this object and objects under it."""

    encryption_details: Optional[EncryptionDetails] = None
    """Encryption options that apply to clients connecting to cloud storage."""

    full_name: Optional[str] = None
    """Full name of table, in form of __catalog_name__.__schema_name__.__table_name__"""

    metastore_id: Optional[str] = None
    """Unique identifier of parent metastore."""

    name: Optional[str] = None
    """Name of table, relative to parent schema."""

    owner: Optional[str] = None
    """Username of current owner of table."""

    pipeline_id: Optional[str] = None
    """The pipeline ID of the table. Applicable for tables created by pipelines (Materialized View,
    Streaming Table, etc.)."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    row_filter: Optional[TableRowFilter] = None

    schema_name: Optional[str] = None
    """Name of parent schema relative to its parent catalog."""

    sql_path: Optional[str] = None
    """List of schemes whose objects can be referenced without qualification."""

    storage_credential_name: Optional[str] = None
    """Name of the storage credential, when a storage credential is configured for use with this table."""

    storage_location: Optional[str] = None
    """Storage root URL for table (for **MANAGED**, **EXTERNAL** tables)"""

    table_constraints: Optional[List[TableConstraint]] = None
    """List of table constraints. Note: this field is not set in the output of the __listTables__ API."""

    table_id: Optional[str] = None
    """Name of table, relative to parent schema."""

    table_type: Optional[TableType] = None

    updated_at: Optional[int] = None
    """Time at which this table was last modified, in epoch milliseconds."""

    updated_by: Optional[str] = None
    """Username of user who last modified the table."""

    view_definition: Optional[str] = None
    """View definition SQL (when __table_type__ is **VIEW**, **MATERIALIZED_VIEW**, or
    **STREAMING_TABLE**)"""

    view_dependencies: Optional[DependencyList] = None
    """View dependencies (when table_type == **VIEW** or **MATERIALIZED_VIEW**, **STREAMING_TABLE**) -
    when DependencyList is None, the dependency is not provided; - when DependencyList is an empty
    list, the dependency is provided but is empty; - when DependencyList is not an empty list,
    dependencies are provided and recorded."""

    def as_dict(self) -> dict:
        """Serializes the TableInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_point is not None: body['access_point'] = self.access_point
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.columns: body['columns'] = [v.as_dict() for v in self.columns]
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.data_access_configuration_id is not None:
            body['data_access_configuration_id'] = self.data_access_configuration_id
        if self.data_source_format is not None: body['data_source_format'] = self.data_source_format.value
        if self.deleted_at is not None: body['deleted_at'] = self.deleted_at
        if self.delta_runtime_properties_kvpairs:
            body['delta_runtime_properties_kvpairs'] = self.delta_runtime_properties_kvpairs.as_dict()
        if self.effective_predictive_optimization_flag:
            body[
                'effective_predictive_optimization_flag'] = self.effective_predictive_optimization_flag.as_dict(
                )
        if self.enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = self.enable_predictive_optimization.value
        if self.encryption_details: body['encryption_details'] = self.encryption_details.as_dict()
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.pipeline_id is not None: body['pipeline_id'] = self.pipeline_id
        if self.properties: body['properties'] = self.properties
        if self.row_filter: body['row_filter'] = self.row_filter.as_dict()
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.sql_path is not None: body['sql_path'] = self.sql_path
        if self.storage_credential_name is not None:
            body['storage_credential_name'] = self.storage_credential_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.table_constraints: body['table_constraints'] = [v.as_dict() for v in self.table_constraints]
        if self.table_id is not None: body['table_id'] = self.table_id
        if self.table_type is not None: body['table_type'] = self.table_type.value
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.view_definition is not None: body['view_definition'] = self.view_definition
        if self.view_dependencies: body['view_dependencies'] = self.view_dependencies.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableInfo:
        """Deserializes the TableInfo from a dictionary."""
        return cls(access_point=d.get('access_point', None),
                   catalog_name=d.get('catalog_name', None),
                   columns=_repeated_dict(d, 'columns', ColumnInfo),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   data_access_configuration_id=d.get('data_access_configuration_id', None),
                   data_source_format=_enum(d, 'data_source_format', DataSourceFormat),
                   deleted_at=d.get('deleted_at', None),
                   delta_runtime_properties_kvpairs=_from_dict(d, 'delta_runtime_properties_kvpairs',
                                                               DeltaRuntimePropertiesKvPairs),
                   effective_predictive_optimization_flag=_from_dict(
                       d, 'effective_predictive_optimization_flag', EffectivePredictiveOptimizationFlag),
                   enable_predictive_optimization=_enum(d, 'enable_predictive_optimization',
                                                        EnablePredictiveOptimization),
                   encryption_details=_from_dict(d, 'encryption_details', EncryptionDetails),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   pipeline_id=d.get('pipeline_id', None),
                   properties=d.get('properties', None),
                   row_filter=_from_dict(d, 'row_filter', TableRowFilter),
                   schema_name=d.get('schema_name', None),
                   sql_path=d.get('sql_path', None),
                   storage_credential_name=d.get('storage_credential_name', None),
                   storage_location=d.get('storage_location', None),
                   table_constraints=_repeated_dict(d, 'table_constraints', TableConstraint),
                   table_id=d.get('table_id', None),
                   table_type=_enum(d, 'table_type', TableType),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   view_definition=d.get('view_definition', None),
                   view_dependencies=_from_dict(d, 'view_dependencies', DependencyList))


@dataclass
class TableRowFilter:
    name: str
    """The full name of the row filter SQL UDF."""

    input_column_names: List[str]
    """The list of table columns to be passed as input to the row filter function. The column types
    should match the types of the filter function arguments."""

    def as_dict(self) -> dict:
        """Serializes the TableRowFilter into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.input_column_names: body['input_column_names'] = [v for v in self.input_column_names]
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableRowFilter:
        """Deserializes the TableRowFilter from a dictionary."""
        return cls(input_column_names=d.get('input_column_names', None), name=d.get('name', None))


@dataclass
class TableSummary:
    full_name: Optional[str] = None
    """The full name of the table."""

    table_type: Optional[TableType] = None

    def as_dict(self) -> dict:
        """Serializes the TableSummary into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.table_type is not None: body['table_type'] = self.table_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TableSummary:
        """Deserializes the TableSummary from a dictionary."""
        return cls(full_name=d.get('full_name', None), table_type=_enum(d, 'table_type', TableType))


class TableType(Enum):

    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'
    MATERIALIZED_VIEW = 'MATERIALIZED_VIEW'
    STREAMING_TABLE = 'STREAMING_TABLE'
    VIEW = 'VIEW'


@dataclass
class TriggeredUpdateStatus:
    """Detailed status of an online table. Shown if the online table is in the ONLINE_TRIGGERED_UPDATE
    or the ONLINE_NO_PENDING_UPDATE state."""

    last_processed_commit_version: Optional[int] = None
    """The last source table Delta version that was synced to the online table. Note that this Delta
    version may not be completely synced to the online table yet."""

    timestamp: Optional[str] = None
    """The timestamp of the last time any data was synchronized from the source table to the online
    table."""

    triggered_update_progress: Optional[PipelineProgress] = None
    """Progress of the active data synchronization pipeline."""

    def as_dict(self) -> dict:
        """Serializes the TriggeredUpdateStatus into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.last_processed_commit_version is not None:
            body['last_processed_commit_version'] = self.last_processed_commit_version
        if self.timestamp is not None: body['timestamp'] = self.timestamp
        if self.triggered_update_progress:
            body['triggered_update_progress'] = self.triggered_update_progress.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TriggeredUpdateStatus:
        """Deserializes the TriggeredUpdateStatus from a dictionary."""
        return cls(last_processed_commit_version=d.get('last_processed_commit_version', None),
                   timestamp=d.get('timestamp', None),
                   triggered_update_progress=_from_dict(d, 'triggered_update_progress', PipelineProgress))


@dataclass
class UnassignResponse:

    def as_dict(self) -> dict:
        """Serializes the UnassignResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UnassignResponse:
        """Deserializes the UnassignResponse from a dictionary."""
        return cls()


@dataclass
class UpdateAssignmentResponse:

    def as_dict(self) -> dict:
        """Serializes the UpdateAssignmentResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateAssignmentResponse:
        """Deserializes the UpdateAssignmentResponse from a dictionary."""
        return cls()


@dataclass
class UpdateCatalog:
    comment: Optional[str] = None
    """User-provided free-form text description."""

    enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None
    """Whether predictive optimization should be enabled for this object and objects under it."""

    isolation_mode: Optional[IsolationMode] = None
    """Whether the current securable is accessible from all workspaces or a specific set of workspaces."""

    name: Optional[str] = None
    """The name of the catalog."""

    new_name: Optional[str] = None
    """New name for the catalog."""

    owner: Optional[str] = None
    """Username of current owner of catalog."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    def as_dict(self) -> dict:
        """Serializes the UpdateCatalog into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = self.enable_predictive_optimization.value
        if self.isolation_mode is not None: body['isolation_mode'] = self.isolation_mode.value
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateCatalog:
        """Deserializes the UpdateCatalog from a dictionary."""
        return cls(comment=d.get('comment', None),
                   enable_predictive_optimization=_enum(d, 'enable_predictive_optimization',
                                                        EnablePredictiveOptimization),
                   isolation_mode=_enum(d, 'isolation_mode', IsolationMode),
                   name=d.get('name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None))


@dataclass
class UpdateConnection:
    options: Dict[str, str]
    """A map of key-value properties attached to the securable."""

    name: Optional[str] = None
    """Name of the connection."""

    new_name: Optional[str] = None
    """New name for the connection."""

    owner: Optional[str] = None
    """Username of current owner of the connection."""

    def as_dict(self) -> dict:
        """Serializes the UpdateConnection into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.options: body['options'] = self.options
        if self.owner is not None: body['owner'] = self.owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateConnection:
        """Deserializes the UpdateConnection from a dictionary."""
        return cls(name=d.get('name', None),
                   new_name=d.get('new_name', None),
                   options=d.get('options', None),
                   owner=d.get('owner', None))


@dataclass
class UpdateExternalLocation:
    access_point: Optional[str] = None
    """The AWS access point to use when accesing s3 for this external location."""

    comment: Optional[str] = None
    """User-provided free-form text description."""

    credential_name: Optional[str] = None
    """Name of the storage credential used with this location."""

    encryption_details: Optional[EncryptionDetails] = None
    """Encryption options that apply to clients connecting to cloud storage."""

    force: Optional[bool] = None
    """Force update even if changing url invalidates dependent external tables or mounts."""

    name: Optional[str] = None
    """Name of the external location."""

    new_name: Optional[str] = None
    """New name for the external location."""

    owner: Optional[str] = None
    """The owner of the external location."""

    read_only: Optional[bool] = None
    """Indicates whether the external location is read-only."""

    skip_validation: Optional[bool] = None
    """Skips validation of the storage credential associated with the external location."""

    url: Optional[str] = None
    """Path URL of the external location."""

    def as_dict(self) -> dict:
        """Serializes the UpdateExternalLocation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_point is not None: body['access_point'] = self.access_point
        if self.comment is not None: body['comment'] = self.comment
        if self.credential_name is not None: body['credential_name'] = self.credential_name
        if self.encryption_details: body['encryption_details'] = self.encryption_details.as_dict()
        if self.force is not None: body['force'] = self.force
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.skip_validation is not None: body['skip_validation'] = self.skip_validation
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateExternalLocation:
        """Deserializes the UpdateExternalLocation from a dictionary."""
        return cls(access_point=d.get('access_point', None),
                   comment=d.get('comment', None),
                   credential_name=d.get('credential_name', None),
                   encryption_details=_from_dict(d, 'encryption_details', EncryptionDetails),
                   force=d.get('force', None),
                   name=d.get('name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None),
                   url=d.get('url', None))


@dataclass
class UpdateFunction:
    name: Optional[str] = None
    """The fully-qualified name of the function (of the form
    __catalog_name__.__schema_name__.__function__name__)."""

    owner: Optional[str] = None
    """Username of current owner of function."""

    def as_dict(self) -> dict:
        """Serializes the UpdateFunction into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateFunction:
        """Deserializes the UpdateFunction from a dictionary."""
        return cls(name=d.get('name', None), owner=d.get('owner', None))


@dataclass
class UpdateMetastore:
    delta_sharing_organization_name: Optional[str] = None
    """The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta
    Sharing as the official name."""

    delta_sharing_recipient_token_lifetime_in_seconds: Optional[int] = None
    """The lifetime of delta sharing recipient token in seconds."""

    delta_sharing_scope: Optional[UpdateMetastoreDeltaSharingScope] = None
    """The scope of Delta Sharing enabled for the metastore."""

    id: Optional[str] = None
    """Unique ID of the metastore."""

    new_name: Optional[str] = None
    """New name for the metastore."""

    owner: Optional[str] = None
    """The owner of the metastore."""

    privilege_model_version: Optional[str] = None
    """Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."""

    storage_root_credential_id: Optional[str] = None
    """UUID of storage credential to access the metastore storage_root."""

    def as_dict(self) -> dict:
        """Serializes the UpdateMetastore into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.delta_sharing_organization_name is not None:
            body['delta_sharing_organization_name'] = self.delta_sharing_organization_name
        if self.delta_sharing_recipient_token_lifetime_in_seconds is not None:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = self.delta_sharing_recipient_token_lifetime_in_seconds
        if self.delta_sharing_scope is not None: body['delta_sharing_scope'] = self.delta_sharing_scope.value
        if self.id is not None: body['id'] = self.id
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        if self.privilege_model_version is not None:
            body['privilege_model_version'] = self.privilege_model_version
        if self.storage_root_credential_id is not None:
            body['storage_root_credential_id'] = self.storage_root_credential_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateMetastore:
        """Deserializes the UpdateMetastore from a dictionary."""
        return cls(delta_sharing_organization_name=d.get('delta_sharing_organization_name', None),
                   delta_sharing_recipient_token_lifetime_in_seconds=d.get(
                       'delta_sharing_recipient_token_lifetime_in_seconds', None),
                   delta_sharing_scope=_enum(d, 'delta_sharing_scope', UpdateMetastoreDeltaSharingScope),
                   id=d.get('id', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None),
                   privilege_model_version=d.get('privilege_model_version', None),
                   storage_root_credential_id=d.get('storage_root_credential_id', None))


@dataclass
class UpdateMetastoreAssignment:
    default_catalog_name: Optional[str] = None
    """The name of the default catalog for the metastore."""

    metastore_id: Optional[str] = None
    """The unique ID of the metastore."""

    workspace_id: Optional[int] = None
    """A workspace ID."""

    def as_dict(self) -> dict:
        """Serializes the UpdateMetastoreAssignment into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.default_catalog_name is not None: body['default_catalog_name'] = self.default_catalog_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateMetastoreAssignment:
        """Deserializes the UpdateMetastoreAssignment from a dictionary."""
        return cls(default_catalog_name=d.get('default_catalog_name', None),
                   metastore_id=d.get('metastore_id', None),
                   workspace_id=d.get('workspace_id', None))


class UpdateMetastoreDeltaSharingScope(Enum):
    """The scope of Delta Sharing enabled for the metastore."""

    INTERNAL = 'INTERNAL'
    INTERNAL_AND_EXTERNAL = 'INTERNAL_AND_EXTERNAL'


@dataclass
class UpdateModelVersionRequest:
    comment: Optional[str] = None
    """The comment attached to the model version"""

    full_name: Optional[str] = None
    """The three-level (fully qualified) name of the model version"""

    version: Optional[int] = None
    """The integer version number of the model version"""

    def as_dict(self) -> dict:
        """Serializes the UpdateModelVersionRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.version is not None: body['version'] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateModelVersionRequest:
        """Deserializes the UpdateModelVersionRequest from a dictionary."""
        return cls(comment=d.get('comment', None),
                   full_name=d.get('full_name', None),
                   version=d.get('version', None))


@dataclass
class UpdateMonitor:
    output_schema_name: str
    """Schema where output metric tables are created."""

    baseline_table_name: Optional[str] = None
    """Name of the baseline table from which drift metrics are computed from. Columns in the monitored
    table should also be present in the baseline table."""

    custom_metrics: Optional[List[MonitorCustomMetric]] = None
    """Custom metrics to compute on the monitored table. These can be aggregate metrics, derived
    metrics (from already computed aggregate metrics), or drift metrics (comparing metrics across
    time windows)."""

    data_classification_config: Optional[MonitorDataClassificationConfig] = None
    """The data classification config for the monitor."""

    full_name: Optional[str] = None
    """Full name of the table."""

    inference_log: Optional[MonitorInferenceLogProfileType] = None
    """Configuration for monitoring inference logs."""

    notifications: Optional[List[MonitorNotificationsConfig]] = None
    """The notification settings for the monitor."""

    schedule: Optional[MonitorCronSchedule] = None
    """The schedule for automatically updating and refreshing metric tables."""

    slicing_exprs: Optional[List[str]] = None
    """List of column expressions to slice data with for targeted analysis. The data is grouped by each
    expression independently, resulting in a separate slice for each predicate and its complements.
    For high-cardinality columns, only the top 100 unique values by frequency will generate slices."""

    snapshot: Optional[MonitorSnapshotProfileType] = None
    """Configuration for monitoring snapshot tables."""

    time_series: Optional[MonitorTimeSeriesProfileType] = None
    """Configuration for monitoring time series tables."""

    def as_dict(self) -> dict:
        """Serializes the UpdateMonitor into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.baseline_table_name is not None: body['baseline_table_name'] = self.baseline_table_name
        if self.custom_metrics: body['custom_metrics'] = [v.as_dict() for v in self.custom_metrics]
        if self.data_classification_config:
            body['data_classification_config'] = self.data_classification_config.as_dict()
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.inference_log: body['inference_log'] = self.inference_log.as_dict()
        if self.notifications: body['notifications'] = [v.as_dict() for v in self.notifications]
        if self.output_schema_name is not None: body['output_schema_name'] = self.output_schema_name
        if self.schedule: body['schedule'] = self.schedule.as_dict()
        if self.slicing_exprs: body['slicing_exprs'] = [v for v in self.slicing_exprs]
        if self.snapshot: body['snapshot'] = self.snapshot.as_dict()
        if self.time_series: body['time_series'] = self.time_series.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateMonitor:
        """Deserializes the UpdateMonitor from a dictionary."""
        return cls(baseline_table_name=d.get('baseline_table_name', None),
                   custom_metrics=_repeated_dict(d, 'custom_metrics', MonitorCustomMetric),
                   data_classification_config=_from_dict(d, 'data_classification_config',
                                                         MonitorDataClassificationConfig),
                   full_name=d.get('full_name', None),
                   inference_log=_from_dict(d, 'inference_log', MonitorInferenceLogProfileType),
                   notifications=_repeated_dict(d, 'notifications', MonitorNotificationsConfig),
                   output_schema_name=d.get('output_schema_name', None),
                   schedule=_from_dict(d, 'schedule', MonitorCronSchedule),
                   slicing_exprs=d.get('slicing_exprs', None),
                   snapshot=_from_dict(d, 'snapshot', MonitorSnapshotProfileType),
                   time_series=_from_dict(d, 'time_series', MonitorTimeSeriesProfileType))


@dataclass
class UpdatePermissions:
    changes: Optional[List[PermissionsChange]] = None
    """Array of permissions change objects."""

    full_name: Optional[str] = None
    """Full name of securable."""

    securable_type: Optional[SecurableType] = None
    """Type of securable."""

    def as_dict(self) -> dict:
        """Serializes the UpdatePermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.changes: body['changes'] = [v.as_dict() for v in self.changes]
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.securable_type is not None: body['securable_type'] = self.securable_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdatePermissions:
        """Deserializes the UpdatePermissions from a dictionary."""
        return cls(changes=_repeated_dict(d, 'changes', PermissionsChange),
                   full_name=d.get('full_name', None),
                   securable_type=_enum(d, 'securable_type', SecurableType))


@dataclass
class UpdateRegisteredModelRequest:
    comment: Optional[str] = None
    """The comment attached to the registered model"""

    full_name: Optional[str] = None
    """The three-level (fully qualified) name of the registered model"""

    new_name: Optional[str] = None
    """New name for the registered model."""

    owner: Optional[str] = None
    """The identifier of the user who owns the registered model"""

    def as_dict(self) -> dict:
        """Serializes the UpdateRegisteredModelRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateRegisteredModelRequest:
        """Deserializes the UpdateRegisteredModelRequest from a dictionary."""
        return cls(comment=d.get('comment', None),
                   full_name=d.get('full_name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None))


@dataclass
class UpdateResponse:

    def as_dict(self) -> dict:
        """Serializes the UpdateResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateResponse:
        """Deserializes the UpdateResponse from a dictionary."""
        return cls()


@dataclass
class UpdateSchema:
    comment: Optional[str] = None
    """User-provided free-form text description."""

    enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None
    """Whether predictive optimization should be enabled for this object and objects under it."""

    full_name: Optional[str] = None
    """Full name of the schema."""

    new_name: Optional[str] = None
    """New name for the schema."""

    owner: Optional[str] = None
    """Username of current owner of schema."""

    properties: Optional[Dict[str, str]] = None
    """A map of key-value properties attached to the securable."""

    def as_dict(self) -> dict:
        """Serializes the UpdateSchema into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = self.enable_predictive_optimization.value
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        if self.properties: body['properties'] = self.properties
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateSchema:
        """Deserializes the UpdateSchema from a dictionary."""
        return cls(comment=d.get('comment', None),
                   enable_predictive_optimization=_enum(d, 'enable_predictive_optimization',
                                                        EnablePredictiveOptimization),
                   full_name=d.get('full_name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None),
                   properties=d.get('properties', None))


@dataclass
class UpdateStorageCredential:
    aws_iam_role: Optional[AwsIamRole] = None
    """The AWS IAM role configuration."""

    azure_managed_identity: Optional[AzureManagedIdentity] = None
    """The Azure managed identity configuration."""

    azure_service_principal: Optional[AzureServicePrincipal] = None
    """The Azure service principal configuration."""

    cloudflare_api_token: Optional[CloudflareApiToken] = None
    """The Cloudflare API token configuration."""

    comment: Optional[str] = None
    """Comment associated with the credential."""

    databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None
    """The <Databricks> managed GCP service account configuration."""

    force: Optional[bool] = None
    """Force update even if there are dependent external locations or external tables."""

    name: Optional[str] = None
    """Name of the storage credential."""

    new_name: Optional[str] = None
    """New name for the storage credential."""

    owner: Optional[str] = None
    """Username of current owner of credential."""

    read_only: Optional[bool] = None
    """Whether the storage credential is only usable for read operations."""

    skip_validation: Optional[bool] = None
    """Supplying true to this argument skips validation of the updated credential."""

    def as_dict(self) -> dict:
        """Serializes the UpdateStorageCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_managed_identity: body['azure_managed_identity'] = self.azure_managed_identity.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.cloudflare_api_token: body['cloudflare_api_token'] = self.cloudflare_api_token.as_dict()
        if self.comment is not None: body['comment'] = self.comment
        if self.databricks_gcp_service_account:
            body['databricks_gcp_service_account'] = self.databricks_gcp_service_account.as_dict()
        if self.force is not None: body['force'] = self.force
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.skip_validation is not None: body['skip_validation'] = self.skip_validation
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateStorageCredential:
        """Deserializes the UpdateStorageCredential from a dictionary."""
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_managed_identity=_from_dict(d, 'azure_managed_identity', AzureManagedIdentity),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   cloudflare_api_token=_from_dict(d, 'cloudflare_api_token', CloudflareApiToken),
                   comment=d.get('comment', None),
                   databricks_gcp_service_account=_from_dict(d, 'databricks_gcp_service_account',
                                                             DatabricksGcpServiceAccountRequest),
                   force=d.get('force', None),
                   name=d.get('name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None),
                   read_only=d.get('read_only', None),
                   skip_validation=d.get('skip_validation', None))


@dataclass
class UpdateVolumeRequestContent:
    comment: Optional[str] = None
    """The comment attached to the volume"""

    name: Optional[str] = None
    """The three-level (fully qualified) name of the volume"""

    new_name: Optional[str] = None
    """New name for the volume."""

    owner: Optional[str] = None
    """The identifier of the user who owns the volume"""

    def as_dict(self) -> dict:
        """Serializes the UpdateVolumeRequestContent into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.comment is not None: body['comment'] = self.comment
        if self.name is not None: body['name'] = self.name
        if self.new_name is not None: body['new_name'] = self.new_name
        if self.owner is not None: body['owner'] = self.owner
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateVolumeRequestContent:
        """Deserializes the UpdateVolumeRequestContent from a dictionary."""
        return cls(comment=d.get('comment', None),
                   name=d.get('name', None),
                   new_name=d.get('new_name', None),
                   owner=d.get('owner', None))


@dataclass
class UpdateWorkspaceBindings:
    assign_workspaces: Optional[List[int]] = None
    """A list of workspace IDs."""

    name: Optional[str] = None
    """The name of the catalog."""

    unassign_workspaces: Optional[List[int]] = None
    """A list of workspace IDs."""

    def as_dict(self) -> dict:
        """Serializes the UpdateWorkspaceBindings into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.assign_workspaces: body['assign_workspaces'] = [v for v in self.assign_workspaces]
        if self.name is not None: body['name'] = self.name
        if self.unassign_workspaces: body['unassign_workspaces'] = [v for v in self.unassign_workspaces]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateWorkspaceBindings:
        """Deserializes the UpdateWorkspaceBindings from a dictionary."""
        return cls(assign_workspaces=d.get('assign_workspaces', None),
                   name=d.get('name', None),
                   unassign_workspaces=d.get('unassign_workspaces', None))


@dataclass
class UpdateWorkspaceBindingsParameters:
    add: Optional[List[WorkspaceBinding]] = None
    """List of workspace bindings"""

    remove: Optional[List[WorkspaceBinding]] = None
    """List of workspace bindings"""

    securable_name: Optional[str] = None
    """The name of the securable."""

    securable_type: Optional[str] = None
    """The type of the securable."""

    def as_dict(self) -> dict:
        """Serializes the UpdateWorkspaceBindingsParameters into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.add: body['add'] = [v.as_dict() for v in self.add]
        if self.remove: body['remove'] = [v.as_dict() for v in self.remove]
        if self.securable_name is not None: body['securable_name'] = self.securable_name
        if self.securable_type is not None: body['securable_type'] = self.securable_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> UpdateWorkspaceBindingsParameters:
        """Deserializes the UpdateWorkspaceBindingsParameters from a dictionary."""
        return cls(add=_repeated_dict(d, 'add', WorkspaceBinding),
                   remove=_repeated_dict(d, 'remove', WorkspaceBinding),
                   securable_name=d.get('securable_name', None),
                   securable_type=d.get('securable_type', None))


@dataclass
class ValidateStorageCredential:
    aws_iam_role: Optional[AwsIamRole] = None
    """The AWS IAM role configuration."""

    azure_managed_identity: Optional[AzureManagedIdentity] = None
    """The Azure managed identity configuration."""

    azure_service_principal: Optional[AzureServicePrincipal] = None
    """The Azure service principal configuration."""

    cloudflare_api_token: Optional[CloudflareApiToken] = None
    """The Cloudflare API token configuration."""

    databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None
    """The Databricks created GCP service account configuration."""

    external_location_name: Optional[str] = None
    """The name of an existing external location to validate."""

    read_only: Optional[bool] = None
    """Whether the storage credential is only usable for read operations."""

    storage_credential_name: Optional[str] = None
    """The name of the storage credential to validate."""

    url: Optional[str] = None
    """The external location url to validate."""

    def as_dict(self) -> dict:
        """Serializes the ValidateStorageCredential into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_iam_role: body['aws_iam_role'] = self.aws_iam_role.as_dict()
        if self.azure_managed_identity: body['azure_managed_identity'] = self.azure_managed_identity.as_dict()
        if self.azure_service_principal:
            body['azure_service_principal'] = self.azure_service_principal.as_dict()
        if self.cloudflare_api_token: body['cloudflare_api_token'] = self.cloudflare_api_token.as_dict()
        if self.databricks_gcp_service_account:
            body['databricks_gcp_service_account'] = self.databricks_gcp_service_account.as_dict()
        if self.external_location_name is not None:
            body['external_location_name'] = self.external_location_name
        if self.read_only is not None: body['read_only'] = self.read_only
        if self.storage_credential_name is not None:
            body['storage_credential_name'] = self.storage_credential_name
        if self.url is not None: body['url'] = self.url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ValidateStorageCredential:
        """Deserializes the ValidateStorageCredential from a dictionary."""
        return cls(aws_iam_role=_from_dict(d, 'aws_iam_role', AwsIamRole),
                   azure_managed_identity=_from_dict(d, 'azure_managed_identity', AzureManagedIdentity),
                   azure_service_principal=_from_dict(d, 'azure_service_principal', AzureServicePrincipal),
                   cloudflare_api_token=_from_dict(d, 'cloudflare_api_token', CloudflareApiToken),
                   databricks_gcp_service_account=_from_dict(d, 'databricks_gcp_service_account',
                                                             DatabricksGcpServiceAccountRequest),
                   external_location_name=d.get('external_location_name', None),
                   read_only=d.get('read_only', None),
                   storage_credential_name=d.get('storage_credential_name', None),
                   url=d.get('url', None))


@dataclass
class ValidateStorageCredentialResponse:
    is_dir: Optional[bool] = None
    """Whether the tested location is a directory in cloud storage."""

    results: Optional[List[ValidationResult]] = None
    """The results of the validation check."""

    def as_dict(self) -> dict:
        """Serializes the ValidateStorageCredentialResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.is_dir is not None: body['isDir'] = self.is_dir
        if self.results: body['results'] = [v.as_dict() for v in self.results]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ValidateStorageCredentialResponse:
        """Deserializes the ValidateStorageCredentialResponse from a dictionary."""
        return cls(is_dir=d.get('isDir', None), results=_repeated_dict(d, 'results', ValidationResult))


@dataclass
class ValidationResult:
    message: Optional[str] = None
    """Error message would exist when the result does not equal to **PASS**."""

    operation: Optional[ValidationResultOperation] = None
    """The operation tested."""

    result: Optional[ValidationResultResult] = None
    """The results of the tested operation."""

    def as_dict(self) -> dict:
        """Serializes the ValidationResult into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.message is not None: body['message'] = self.message
        if self.operation is not None: body['operation'] = self.operation.value
        if self.result is not None: body['result'] = self.result.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ValidationResult:
        """Deserializes the ValidationResult from a dictionary."""
        return cls(message=d.get('message', None),
                   operation=_enum(d, 'operation', ValidationResultOperation),
                   result=_enum(d, 'result', ValidationResultResult))


class ValidationResultOperation(Enum):
    """The operation tested."""

    DELETE = 'DELETE'
    LIST = 'LIST'
    READ = 'READ'
    WRITE = 'WRITE'


class ValidationResultResult(Enum):
    """The results of the tested operation."""

    FAIL = 'FAIL'
    PASS = 'PASS'
    SKIP = 'SKIP'


@dataclass
class ViewData:
    """Online Table information."""

    name: Optional[str] = None
    """Full three-part (catalog, schema, table) name of the table."""

    spec: Optional[OnlineTableSpec] = None
    """Specification of the online table."""

    def as_dict(self) -> dict:
        """Serializes the ViewData into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.spec: body['spec'] = self.spec.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ViewData:
        """Deserializes the ViewData from a dictionary."""
        return cls(name=d.get('name', None), spec=_from_dict(d, 'spec', OnlineTableSpec))


@dataclass
class VolumeInfo:
    access_point: Optional[str] = None
    """The AWS access point to use when accesing s3 for this external location."""

    catalog_name: Optional[str] = None
    """The name of the catalog where the schema and the volume are"""

    comment: Optional[str] = None
    """The comment attached to the volume"""

    created_at: Optional[int] = None

    created_by: Optional[str] = None
    """The identifier of the user who created the volume"""

    encryption_details: Optional[EncryptionDetails] = None
    """Encryption options that apply to clients connecting to cloud storage."""

    full_name: Optional[str] = None
    """The three-level (fully qualified) name of the volume"""

    metastore_id: Optional[str] = None
    """The unique identifier of the metastore"""

    name: Optional[str] = None
    """The name of the volume"""

    owner: Optional[str] = None
    """The identifier of the user who owns the volume"""

    schema_name: Optional[str] = None
    """The name of the schema where the volume is"""

    storage_location: Optional[str] = None
    """The storage location on the cloud"""

    updated_at: Optional[int] = None

    updated_by: Optional[str] = None
    """The identifier of the user who updated the volume last time"""

    volume_id: Optional[str] = None
    """The unique identifier of the volume"""

    volume_type: Optional[VolumeType] = None

    def as_dict(self) -> dict:
        """Serializes the VolumeInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_point is not None: body['access_point'] = self.access_point
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.comment is not None: body['comment'] = self.comment
        if self.created_at is not None: body['created_at'] = self.created_at
        if self.created_by is not None: body['created_by'] = self.created_by
        if self.encryption_details: body['encryption_details'] = self.encryption_details.as_dict()
        if self.full_name is not None: body['full_name'] = self.full_name
        if self.metastore_id is not None: body['metastore_id'] = self.metastore_id
        if self.name is not None: body['name'] = self.name
        if self.owner is not None: body['owner'] = self.owner
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.storage_location is not None: body['storage_location'] = self.storage_location
        if self.updated_at is not None: body['updated_at'] = self.updated_at
        if self.updated_by is not None: body['updated_by'] = self.updated_by
        if self.volume_id is not None: body['volume_id'] = self.volume_id
        if self.volume_type is not None: body['volume_type'] = self.volume_type.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> VolumeInfo:
        """Deserializes the VolumeInfo from a dictionary."""
        return cls(access_point=d.get('access_point', None),
                   catalog_name=d.get('catalog_name', None),
                   comment=d.get('comment', None),
                   created_at=d.get('created_at', None),
                   created_by=d.get('created_by', None),
                   encryption_details=_from_dict(d, 'encryption_details', EncryptionDetails),
                   full_name=d.get('full_name', None),
                   metastore_id=d.get('metastore_id', None),
                   name=d.get('name', None),
                   owner=d.get('owner', None),
                   schema_name=d.get('schema_name', None),
                   storage_location=d.get('storage_location', None),
                   updated_at=d.get('updated_at', None),
                   updated_by=d.get('updated_by', None),
                   volume_id=d.get('volume_id', None),
                   volume_type=_enum(d, 'volume_type', VolumeType))


class VolumeType(Enum):

    EXTERNAL = 'EXTERNAL'
    MANAGED = 'MANAGED'


@dataclass
class WorkspaceBinding:
    binding_type: Optional[WorkspaceBindingBindingType] = None

    workspace_id: Optional[int] = None

    def as_dict(self) -> dict:
        """Serializes the WorkspaceBinding into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.binding_type is not None: body['binding_type'] = self.binding_type.value
        if self.workspace_id is not None: body['workspace_id'] = self.workspace_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WorkspaceBinding:
        """Deserializes the WorkspaceBinding from a dictionary."""
        return cls(binding_type=_enum(d, 'binding_type', WorkspaceBindingBindingType),
                   workspace_id=d.get('workspace_id', None))


class WorkspaceBindingBindingType(Enum):

    BINDING_TYPE_READ_ONLY = 'BINDING_TYPE_READ_ONLY'
    BINDING_TYPE_READ_WRITE = 'BINDING_TYPE_READ_WRITE'


@dataclass
class WorkspaceBindingsResponse:
    """Currently assigned workspace bindings"""

    bindings: Optional[List[WorkspaceBinding]] = None
    """List of workspace bindings"""

    def as_dict(self) -> dict:
        """Serializes the WorkspaceBindingsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bindings: body['bindings'] = [v.as_dict() for v in self.bindings]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> WorkspaceBindingsResponse:
        """Deserializes the WorkspaceBindingsResponse from a dictionary."""
        return cls(bindings=_repeated_dict(d, 'bindings', WorkspaceBinding))


class AccountMetastoreAssignmentsAPI:
    """These APIs manage metastore assignments to a workspace."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               workspace_id: int,
               metastore_id: str,
               *,
               metastore_assignment: Optional[CreateMetastoreAssignment] = None):
        """Assigns a workspace to a metastore.
        
        Creates an assignment to a metastore for a workspace
        
        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_assignment: :class:`CreateMetastoreAssignment` (optional)
        
        
        """
        body = {}
        if metastore_assignment is not None: body['metastore_assignment'] = metastore_assignment.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/metastores/{metastore_id}',
            body=body,
            headers=headers)

    def delete(self, workspace_id: int, metastore_id: str):
        """Delete a metastore assignment.
        
        Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.
        
        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/metastores/{metastore_id}',
            headers=headers)

    def get(self, workspace_id: int) -> AccountsMetastoreAssignment:
        """Gets the metastore assignment for a workspace.
        
        Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned
        a metastore, the mappig will be returned. If no metastore is assigned to the workspace, the assignment
        will not be found and a 404 returned.
        
        :param workspace_id: int
          Workspace ID.
        
        :returns: :class:`AccountsMetastoreAssignment`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/metastore',
                           headers=headers)
        return AccountsMetastoreAssignment.from_dict(res)

    def list(self, metastore_id: str) -> Iterator[int]:
        """Get all workspaces assigned to a metastore.
        
        Gets a list of all Databricks workspace IDs that have been assigned to given metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: Iterator over int
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET',
                            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/workspaces',
                            headers=headers)
        parsed = ListAccountMetastoreAssignmentsResponse.from_dict(json).workspace_ids
        return parsed if parsed is not None else []

    def update(self,
               workspace_id: int,
               metastore_id: str,
               *,
               metastore_assignment: Optional[UpdateMetastoreAssignment] = None):
        """Updates a metastore assignment to a workspaces.
        
        Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be
        updated.
        
        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_assignment: :class:`UpdateMetastoreAssignment` (optional)
        
        
        """
        body = {}
        if metastore_assignment is not None: body['metastore_assignment'] = metastore_assignment.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/workspaces/{workspace_id}/metastores/{metastore_id}',
            body=body,
            headers=headers)


class AccountMetastoresAPI:
    """These APIs manage Unity Catalog metastores for an account. A metastore contains catalogs that can be
    associated with workspaces"""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, metastore_info: Optional[CreateMetastore] = None) -> AccountsMetastoreInfo:
        """Create metastore.
        
        Creates a Unity Catalog metastore.
        
        :param metastore_info: :class:`CreateMetastore` (optional)
        
        :returns: :class:`AccountsMetastoreInfo`
        """
        body = {}
        if metastore_info is not None: body['metastore_info'] = metastore_info.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.0/accounts/{self._api.account_id}/metastores',
                           body=body,
                           headers=headers)
        return AccountsMetastoreInfo.from_dict(res)

    def delete(self, metastore_id: str, *, force: Optional[bool] = None):
        """Delete a metastore.
        
        Deletes a Unity Catalog metastore for an account, both specified by ID.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param force: bool (optional)
          Force deletion even if the metastore is not empty. Default is false.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}',
                     query=query,
                     headers=headers)

    def get(self, metastore_id: str) -> AccountsMetastoreInfo:
        """Get a metastore.
        
        Gets a Unity Catalog metastore from an account, both specified by ID.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: :class:`AccountsMetastoreInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}',
                           headers=headers)
        return AccountsMetastoreInfo.from_dict(res)

    def list(self) -> Iterator[MetastoreInfo]:
        """Get all metastores associated with an account.
        
        Gets all Unity Catalog metastores associated with an account specified by ID.
        
        :returns: Iterator over :class:`MetastoreInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', f'/api/2.0/accounts/{self._api.account_id}/metastores', headers=headers)
        parsed = ListMetastoresResponse.from_dict(json).metastores
        return parsed if parsed is not None else []

    def update(self,
               metastore_id: str,
               *,
               metastore_info: Optional[UpdateMetastore] = None) -> AccountsMetastoreInfo:
        """Update a metastore.
        
        Updates an existing Unity Catalog metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_info: :class:`UpdateMetastore` (optional)
        
        :returns: :class:`AccountsMetastoreInfo`
        """
        body = {}
        if metastore_info is not None: body['metastore_info'] = metastore_info.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}',
                           body=body,
                           headers=headers)
        return AccountsMetastoreInfo.from_dict(res)


class AccountStorageCredentialsAPI:
    """These APIs manage storage credentials for a particular metastore."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               metastore_id: str,
               *,
               credential_info: Optional[CreateStorageCredential] = None) -> AccountsStorageCredentialInfo:
        """Create a storage credential.
        
        Creates a new storage credential. The request object is specific to the cloud:
        
        * **AwsIamRole** for AWS credentials * **AzureServicePrincipal** for Azure credentials *
        **GcpServiceAcountKey** for GCP credentials.
        
        The caller must be a metastore admin and have the **CREATE_STORAGE_CREDENTIAL** privilege on the
        metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param credential_info: :class:`CreateStorageCredential` (optional)
        
        :returns: :class:`AccountsStorageCredentialInfo`
        """
        body = {}
        if credential_info is not None: body['credential_info'] = credential_info.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'POST',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/storage-credentials',
            body=body,
            headers=headers)
        return AccountsStorageCredentialInfo.from_dict(res)

    def delete(self, metastore_id: str, storage_credential_name: str, *, force: Optional[bool] = None):
        """Delete a storage credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        :param force: bool (optional)
          Force deletion even if the Storage Credential is not empty. Default is false.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do(
            'DELETE',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/storage-credentials/{storage_credential_name}',
            query=query,
            headers=headers)

    def get(self, metastore_id: str, storage_credential_name: str) -> AccountsStorageCredentialInfo:
        """Gets the named storage credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have a level of privilege on the storage credential.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        
        :returns: :class:`AccountsStorageCredentialInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/storage-credentials/{storage_credential_name}',
            headers=headers)
        return AccountsStorageCredentialInfo.from_dict(res)

    def list(self, metastore_id: str) -> Iterator[StorageCredentialInfo]:
        """Get all storage credentials assigned to a metastore.
        
        Gets a list of all storage credentials that have been assigned to given metastore.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        
        :returns: Iterator over :class:`StorageCredentialInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do(
            'GET',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/storage-credentials',
            headers=headers)
        return [StorageCredentialInfo.from_dict(v) for v in res]

    def update(self,
               metastore_id: str,
               storage_credential_name: str,
               *,
               credential_info: Optional[UpdateStorageCredential] = None) -> AccountsStorageCredentialInfo:
        """Updates a storage credential.
        
        Updates a storage credential on the metastore. The caller must be the owner of the storage credential.
        If the caller is a metastore admin, only the __owner__ credential can be changed.
        
        :param metastore_id: str
          Unity Catalog metastore ID
        :param storage_credential_name: str
          Name of the storage credential.
        :param credential_info: :class:`UpdateStorageCredential` (optional)
        
        :returns: :class:`AccountsStorageCredentialInfo`
        """
        body = {}
        if credential_info is not None: body['credential_info'] = credential_info.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do(
            'PUT',
            f'/api/2.0/accounts/{self._api.account_id}/metastores/{metastore_id}/storage-credentials/{storage_credential_name}',
            body=body,
            headers=headers)
        return AccountsStorageCredentialInfo.from_dict(res)


class ArtifactAllowlistsAPI:
    """In Databricks Runtime 13.3 and above, you can add libraries and init scripts to the `allowlist` in UC so
    that users can leverage these artifacts on compute configured with shared access mode."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, artifact_type: ArtifactType) -> ArtifactAllowlistInfo:
        """Get an artifact allowlist.
        
        Get the artifact allowlist of a certain artifact type. The caller must be a metastore admin or have
        the **MANAGE ALLOWLIST** privilege on the metastore.
        
        :param artifact_type: :class:`ArtifactType`
          The artifact type of the allowlist.
        
        :returns: :class:`ArtifactAllowlistInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/artifact-allowlists/{artifact_type.value}',
                           headers=headers)
        return ArtifactAllowlistInfo.from_dict(res)

    def update(self, artifact_type: ArtifactType,
               artifact_matchers: List[ArtifactMatcher]) -> ArtifactAllowlistInfo:
        """Set an artifact allowlist.
        
        Set the artifact allowlist of a certain artifact type. The whole artifact allowlist is replaced with
        the new allowlist. The caller must be a metastore admin or have the **MANAGE ALLOWLIST** privilege on
        the metastore.
        
        :param artifact_type: :class:`ArtifactType`
          The artifact type of the allowlist.
        :param artifact_matchers: List[:class:`ArtifactMatcher`]
          A list of allowed artifact match patterns.
        
        :returns: :class:`ArtifactAllowlistInfo`
        """
        body = {}
        if artifact_matchers is not None: body['artifact_matchers'] = [v.as_dict() for v in artifact_matchers]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.1/unity-catalog/artifact-allowlists/{artifact_type.value}',
                           body=body,
                           headers=headers)
        return ArtifactAllowlistInfo.from_dict(res)


class CatalogsAPI:
    """A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data
    assets. Users can see all catalogs on which they have been assigned the USE_CATALOG data permission.
    
    In Unity Catalog, admins and data stewards manage users and their access to data centrally across all of
    the workspaces in a Databricks account. Users in different workspaces can share access to the same data,
    depending on privileges granted centrally in Unity Catalog."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               comment: Optional[str] = None,
               connection_name: Optional[str] = None,
               options: Optional[Dict[str, str]] = None,
               properties: Optional[Dict[str, str]] = None,
               provider_name: Optional[str] = None,
               share_name: Optional[str] = None,
               storage_root: Optional[str] = None) -> CatalogInfo:
        """Create a catalog.
        
        Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the
        **CREATE_CATALOG** privilege.
        
        :param name: str
          Name of catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param connection_name: str (optional)
          The name of the connection to an external data source.
        :param options: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param provider_name: str (optional)
          The name of delta sharing provider.
          
          A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server.
        :param share_name: str (optional)
          The name of the share under the share provider.
        :param storage_root: str (optional)
          Storage root URL for managed tables within catalog.
        
        :returns: :class:`CatalogInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if connection_name is not None: body['connection_name'] = connection_name
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if properties is not None: body['properties'] = properties
        if provider_name is not None: body['provider_name'] = provider_name
        if share_name is not None: body['share_name'] = share_name
        if storage_root is not None: body['storage_root'] = storage_root
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/catalogs', body=body, headers=headers)
        return CatalogInfo.from_dict(res)

    def delete(self, name: str, *, force: Optional[bool] = None):
        """Delete a catalog.
        
        Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner
        of the catalog.
        
        :param name: str
          The name of the catalog.
        :param force: bool (optional)
          Force deletion even if the catalog is not empty.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/catalogs/{name}', query=query, headers=headers)

    def get(self, name: str) -> CatalogInfo:
        """Get a catalog.
        
        Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the
        catalog, or a user that has the **USE_CATALOG** privilege set for their account.
        
        :param name: str
          The name of the catalog.
        
        :returns: :class:`CatalogInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/catalogs/{name}', headers=headers)
        return CatalogInfo.from_dict(res)

    def list(self) -> Iterator[CatalogInfo]:
        """List catalogs.
        
        Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be
        retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the
        **USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the
        elements in the array.
        
        :returns: Iterator over :class:`CatalogInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.1/unity-catalog/catalogs', headers=headers)
        parsed = ListCatalogsResponse.from_dict(json).catalogs
        return parsed if parsed is not None else []

    def update(self,
               name: str,
               *,
               comment: Optional[str] = None,
               enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None,
               isolation_mode: Optional[IsolationMode] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None,
               properties: Optional[Dict[str, str]] = None) -> CatalogInfo:
        """Update a catalog.
        
        Updates the catalog that matches the supplied name. The caller must be either the owner of the
        catalog, or a metastore admin (when changing the owner field of the catalog).
        
        :param name: str
          The name of the catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)
          Whether predictive optimization should be enabled for this object and objects under it.
        :param isolation_mode: :class:`IsolationMode` (optional)
          Whether the current securable is accessible from all workspaces or a specific set of workspaces.
        :param new_name: str (optional)
          New name for the catalog.
        :param owner: str (optional)
          Username of current owner of catalog.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        
        :returns: :class:`CatalogInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = enable_predictive_optimization.value
        if isolation_mode is not None: body['isolation_mode'] = isolation_mode.value
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        if properties is not None: body['properties'] = properties
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/catalogs/{name}', body=body, headers=headers)
        return CatalogInfo.from_dict(res)


class ConnectionsAPI:
    """Connections allow for creating a connection to an external data source.
    
    A connection is an abstraction of an external data source that can be connected from Databricks Compute.
    Creating a connection object is the first step to managing external data sources within Unity Catalog,
    with the second step being creating a data object (catalog, schema, or table) using the connection. Data
    objects derived from a connection can be written to or read from similar to other Unity Catalog data
    objects based on cloud storage. Users may create different types of connections with each connection
    having a unique set of configuration options to support credential management and other settings."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               connection_type: ConnectionType,
               options: Dict[str, str],
               *,
               comment: Optional[str] = None,
               properties: Optional[Dict[str, str]] = None,
               read_only: Optional[bool] = None) -> ConnectionInfo:
        """Create a connection.
        
        Creates a new connection
        
        Creates a new connection to an external data source. It allows users to specify connection details and
        configurations for interaction with the external server.
        
        :param name: str
          Name of the connection.
        :param connection_type: :class:`ConnectionType`
          The type of connection.
        :param options: Dict[str,str]
          A map of key-value properties attached to the securable.
        :param comment: str (optional)
          User-provided free-form text description.
        :param properties: Dict[str,str] (optional)
          An object containing map of key-value properties attached to the connection.
        :param read_only: bool (optional)
          If the connection is read only.
        
        :returns: :class:`ConnectionInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if connection_type is not None: body['connection_type'] = connection_type.value
        if name is not None: body['name'] = name
        if options is not None: body['options'] = options
        if properties is not None: body['properties'] = properties
        if read_only is not None: body['read_only'] = read_only
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/connections', body=body, headers=headers)
        return ConnectionInfo.from_dict(res)

    def delete(self, name: str):
        """Delete a connection.
        
        Deletes the connection that matches the supplied name.
        
        :param name: str
          The name of the connection to be deleted.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/connections/{name}', headers=headers)

    def get(self, name: str) -> ConnectionInfo:
        """Get a connection.
        
        Gets a connection from it's name.
        
        :param name: str
          Name of the connection.
        
        :returns: :class:`ConnectionInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/connections/{name}', headers=headers)
        return ConnectionInfo.from_dict(res)

    def list(self) -> Iterator[ConnectionInfo]:
        """List connections.
        
        List all connections.
        
        :returns: Iterator over :class:`ConnectionInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.1/unity-catalog/connections', headers=headers)
        parsed = ListConnectionsResponse.from_dict(json).connections
        return parsed if parsed is not None else []

    def update(self,
               name: str,
               options: Dict[str, str],
               *,
               new_name: Optional[str] = None,
               owner: Optional[str] = None) -> ConnectionInfo:
        """Update a connection.
        
        Updates the connection that matches the supplied name.
        
        :param name: str
          Name of the connection.
        :param options: Dict[str,str]
          A map of key-value properties attached to the securable.
        :param new_name: str (optional)
          New name for the connection.
        :param owner: str (optional)
          Username of current owner of the connection.
        
        :returns: :class:`ConnectionInfo`
        """
        body = {}
        if new_name is not None: body['new_name'] = new_name
        if options is not None: body['options'] = options
        if owner is not None: body['owner'] = owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/connections/{name}', body=body, headers=headers)
        return ConnectionInfo.from_dict(res)


class ExternalLocationsAPI:
    """An external location is an object that combines a cloud storage path with a storage credential that
    authorizes access to the cloud storage path. Each external location is subject to Unity Catalog
    access-control policies that control which users and groups can access the credential. If a user does not
    have access to an external location in Unity Catalog, the request fails and Unity Catalog does not attempt
    to authenticate to your cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create external locations, you must be a metastore admin or a user with the
    **CREATE_EXTERNAL_LOCATION** privilege."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               url: str,
               credential_name: str,
               *,
               access_point: Optional[str] = None,
               comment: Optional[str] = None,
               encryption_details: Optional[EncryptionDetails] = None,
               read_only: Optional[bool] = None,
               skip_validation: Optional[bool] = None) -> ExternalLocationInfo:
        """Create an external location.
        
        Creates a new external location entry in the metastore. The caller must be a metastore admin or have
        the **CREATE_EXTERNAL_LOCATION** privilege on both the metastore and the associated storage
        credential.
        
        :param name: str
          Name of the external location.
        :param url: str
          Path URL of the external location.
        :param credential_name: str
          Name of the storage credential used with this location.
        :param access_point: str (optional)
          The AWS access point to use when accesing s3 for this external location.
        :param comment: str (optional)
          User-provided free-form text description.
        :param encryption_details: :class:`EncryptionDetails` (optional)
          Encryption options that apply to clients connecting to cloud storage.
        :param read_only: bool (optional)
          Indicates whether the external location is read-only.
        :param skip_validation: bool (optional)
          Skips validation of the storage credential associated with the external location.
        
        :returns: :class:`ExternalLocationInfo`
        """
        body = {}
        if access_point is not None: body['access_point'] = access_point
        if comment is not None: body['comment'] = comment
        if credential_name is not None: body['credential_name'] = credential_name
        if encryption_details is not None: body['encryption_details'] = encryption_details.as_dict()
        if name is not None: body['name'] = name
        if read_only is not None: body['read_only'] = read_only
        if skip_validation is not None: body['skip_validation'] = skip_validation
        if url is not None: body['url'] = url
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/external-locations', body=body, headers=headers)
        return ExternalLocationInfo.from_dict(res)

    def delete(self, name: str, *, force: Optional[bool] = None):
        """Delete an external location.
        
        Deletes the specified external location from the metastore. The caller must be the owner of the
        external location.
        
        :param name: str
          Name of the external location.
        :param force: bool (optional)
          Force deletion even if there are dependent external tables or mounts.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/external-locations/{name}',
                     query=query,
                     headers=headers)

    def get(self, name: str) -> ExternalLocationInfo:
        """Get an external location.
        
        Gets an external location from the metastore. The caller must be either a metastore admin, the owner
        of the external location, or a user that has some privilege on the external location.
        
        :param name: str
          Name of the external location.
        
        :returns: :class:`ExternalLocationInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/external-locations/{name}', headers=headers)
        return ExternalLocationInfo.from_dict(res)

    def list(self,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[ExternalLocationInfo]:
        """List external locations.
        
        Gets an array of external locations (__ExternalLocationInfo__ objects) from the metastore. The caller
        must be a metastore admin, the owner of the external location, or a user that has some privilege on
        the external location. For unpaginated request, there is no guarantee of a specific ordering of the
        elements in the array. For paginated request, elements are ordered by their name.
        
        :param max_results: int (optional)
          Maximum number of external locations to return. If not set, all the external locations are returned
          (not recommended). - when set to a value greater than 0, the page length is the minimum of this
          value and a server configured value; - when set to 0, the page length is set to a server configured
          value (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ExternalLocationInfo`
        """

        query = {}
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                '/api/2.1/unity-catalog/external-locations',
                                query=query,
                                headers=headers)
            if 'external_locations' in json:
                for v in json['external_locations']:
                    yield ExternalLocationInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self,
               name: str,
               *,
               access_point: Optional[str] = None,
               comment: Optional[str] = None,
               credential_name: Optional[str] = None,
               encryption_details: Optional[EncryptionDetails] = None,
               force: Optional[bool] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None,
               read_only: Optional[bool] = None,
               skip_validation: Optional[bool] = None,
               url: Optional[str] = None) -> ExternalLocationInfo:
        """Update an external location.
        
        Updates an external location in the metastore. The caller must be the owner of the external location,
        or be a metastore admin. In the second case, the admin can only update the name of the external
        location.
        
        :param name: str
          Name of the external location.
        :param access_point: str (optional)
          The AWS access point to use when accesing s3 for this external location.
        :param comment: str (optional)
          User-provided free-form text description.
        :param credential_name: str (optional)
          Name of the storage credential used with this location.
        :param encryption_details: :class:`EncryptionDetails` (optional)
          Encryption options that apply to clients connecting to cloud storage.
        :param force: bool (optional)
          Force update even if changing url invalidates dependent external tables or mounts.
        :param new_name: str (optional)
          New name for the external location.
        :param owner: str (optional)
          The owner of the external location.
        :param read_only: bool (optional)
          Indicates whether the external location is read-only.
        :param skip_validation: bool (optional)
          Skips validation of the storage credential associated with the external location.
        :param url: str (optional)
          Path URL of the external location.
        
        :returns: :class:`ExternalLocationInfo`
        """
        body = {}
        if access_point is not None: body['access_point'] = access_point
        if comment is not None: body['comment'] = comment
        if credential_name is not None: body['credential_name'] = credential_name
        if encryption_details is not None: body['encryption_details'] = encryption_details.as_dict()
        if force is not None: body['force'] = force
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        if read_only is not None: body['read_only'] = read_only
        if skip_validation is not None: body['skip_validation'] = skip_validation
        if url is not None: body['url'] = url
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/external-locations/{name}',
                           body=body,
                           headers=headers)
        return ExternalLocationInfo.from_dict(res)


class FunctionsAPI:
    """Functions implement User-Defined Functions (UDFs) in Unity Catalog.
    
    The function implementation can be any SQL expression or Query, and it can be invoked wherever a table
    reference is allowed in a query. In Unity Catalog, a function resides at the same level as a table, so it
    can be referenced with the form __catalog_name__.__schema_name__.__function_name__."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, function_info: CreateFunction) -> FunctionInfo:
        """Create a function.
        
        Creates a new function
        
        The user must have the following permissions in order for the function to be created: -
        **USE_CATALOG** on the function's parent catalog - **USE_SCHEMA** and **CREATE_FUNCTION** on the
        function's parent schema
        
        :param function_info: :class:`CreateFunction`
          Partial __FunctionInfo__ specifying the function to be created.
        
        :returns: :class:`FunctionInfo`
        """
        body = {}
        if function_info is not None: body['function_info'] = function_info.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/functions', body=body, headers=headers)
        return FunctionInfo.from_dict(res)

    def delete(self, name: str, *, force: Optional[bool] = None):
        """Delete a function.
        
        Deletes the function that matches the supplied name. For the deletion to succeed, the user must
        satisfy one of the following conditions: - Is the owner of the function's parent catalog - Is the
        owner of the function's parent schema and have the **USE_CATALOG** privilege on its parent catalog -
        Is the owner of the function itself and have both the **USE_CATALOG** privilege on its parent catalog
        and the **USE_SCHEMA** privilege on its parent schema
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        :param force: bool (optional)
          Force deletion even if the function is notempty.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/functions/{name}', query=query, headers=headers)

    def get(self, name: str) -> FunctionInfo:
        """Get a function.
        
        Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must
        satisfy one of the following requirements: - Is a metastore admin - Is an owner of the function's
        parent catalog - Have the **USE_CATALOG** privilege on the function's parent catalog and be the owner
        of the function - Have the **USE_CATALOG** privilege on the function's parent catalog, the
        **USE_SCHEMA** privilege on the function's parent schema, and the **EXECUTE** privilege on the
        function itself
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        
        :returns: :class:`FunctionInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/functions/{name}', headers=headers)
        return FunctionInfo.from_dict(res)

    def list(self,
             catalog_name: str,
             schema_name: str,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[FunctionInfo]:
        """List functions.
        
        List functions within the specified parent catalog and schema. If the user is a metastore admin, all
        functions are returned in the output list. Otherwise, the user must have the **USE_CATALOG** privilege
        on the catalog and the **USE_SCHEMA** privilege on the schema, and the output list contains only
        functions for which either the user has the **EXECUTE** privilege or the user is the owner. For
        unpaginated request, there is no guarantee of a specific ordering of the elements in the array. For
        paginated request, elements are ordered by their name.
        
        :param catalog_name: str
          Name of parent catalog for functions of interest.
        :param schema_name: str
          Parent schema of functions.
        :param max_results: int (optional)
          Maximum number of functions to return. If not set, all the functions are returned (not recommended).
          - when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`FunctionInfo`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        if schema_name is not None: query['schema_name'] = schema_name
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/functions', query=query, headers=headers)
            if 'functions' in json:
                for v in json['functions']:
                    yield FunctionInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self, name: str, *, owner: Optional[str] = None) -> FunctionInfo:
        """Update a function.
        
        Updates the function that matches the supplied name. Only the owner of the function can be updated. If
        the user is not a metastore admin, the user must be a member of the group that is the new function
        owner. - Is a metastore admin - Is the owner of the function's parent catalog - Is the owner of the
        function's parent schema and has the **USE_CATALOG** privilege on its parent catalog - Is the owner of
        the function itself and has the **USE_CATALOG** privilege on its parent catalog as well as the
        **USE_SCHEMA** privilege on the function's parent schema.
        
        :param name: str
          The fully-qualified name of the function (of the form
          __catalog_name__.__schema_name__.__function__name__).
        :param owner: str (optional)
          Username of current owner of function.
        
        :returns: :class:`FunctionInfo`
        """
        body = {}
        if owner is not None: body['owner'] = owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/functions/{name}', body=body, headers=headers)
        return FunctionInfo.from_dict(res)


class GrantsAPI:
    """In Unity Catalog, data is secure by default. Initially, users have no access to data in a metastore.
    Access can be granted by either a metastore admin, the owner of an object, or the owner of the catalog or
    schema that contains the object. Securable objects in Unity Catalog are hierarchical and privileges are
    inherited downward.
    
    Securable objects in Unity Catalog are hierarchical and privileges are inherited downward. This means that
    granting a privilege on the catalog automatically grants the privilege to all current and future objects
    within the catalog. Similarly, privileges granted on a schema are inherited by all current and future
    objects within that schema."""

    def __init__(self, api_client):
        self._api = api_client

    def get(self,
            securable_type: SecurableType,
            full_name: str,
            *,
            principal: Optional[str] = None) -> PermissionsList:
        """Get permissions.
        
        Gets the permissions for a securable.
        
        :param securable_type: :class:`SecurableType`
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param principal: str (optional)
          If provided, only the permissions for the specified principal (user or group) are returned.
        
        :returns: :class:`PermissionsList`
        """

        query = {}
        if principal is not None: query['principal'] = principal
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/permissions/{securable_type.value}/{full_name}',
                           query=query,
                           headers=headers)
        return PermissionsList.from_dict(res)

    def get_effective(self,
                      securable_type: SecurableType,
                      full_name: str,
                      *,
                      principal: Optional[str] = None) -> EffectivePermissionsList:
        """Get effective permissions.
        
        Gets the effective permissions for a securable.
        
        :param securable_type: :class:`SecurableType`
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param principal: str (optional)
          If provided, only the effective permissions for the specified principal (user or group) are
          returned.
        
        :returns: :class:`EffectivePermissionsList`
        """

        query = {}
        if principal is not None: query['principal'] = principal
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/effective-permissions/{securable_type.value}/{full_name}',
                           query=query,
                           headers=headers)
        return EffectivePermissionsList.from_dict(res)

    def update(self,
               securable_type: SecurableType,
               full_name: str,
               *,
               changes: Optional[List[PermissionsChange]] = None) -> PermissionsList:
        """Update permissions.
        
        Updates the permissions for a securable.
        
        :param securable_type: :class:`SecurableType`
          Type of securable.
        :param full_name: str
          Full name of securable.
        :param changes: List[:class:`PermissionsChange`] (optional)
          Array of permissions change objects.
        
        :returns: :class:`PermissionsList`
        """
        body = {}
        if changes is not None: body['changes'] = [v.as_dict() for v in changes]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/permissions/{securable_type.value}/{full_name}',
                           body=body,
                           headers=headers)
        return PermissionsList.from_dict(res)


class LakehouseMonitorsAPI:
    """A monitor computes and monitors data or model quality metrics for a table over time. It generates metrics
    tables and a dashboard that you can use to monitor table health and set alerts.
    
    Most write operations require the user to be the owner of the table (or its parent schema or parent
    catalog). Viewing the dashboard, computed metrics, or monitor configuration only requires the user to have
    **SELECT** privileges on the table (along with **USE_SCHEMA** and **USE_CATALOG**)."""

    def __init__(self, api_client):
        self._api = api_client

    def cancel_refresh(self, full_name: str, refresh_id: str):
        """Cancel refresh.
        
        Cancel an active monitor refresh for the given refresh ID.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param full_name: str
          Full name of the table.
        :param refresh_id: str
          ID of the refresh.
        
        
        """

        headers = {}

        self._api.do('POST',
                     f'/api/2.1/unity-catalog/tables/{full_name}/monitor/refreshes/{refresh_id}/cancel',
                     headers=headers)

    def create(self,
               full_name: str,
               assets_dir: str,
               output_schema_name: str,
               *,
               baseline_table_name: Optional[str] = None,
               custom_metrics: Optional[List[MonitorCustomMetric]] = None,
               data_classification_config: Optional[MonitorDataClassificationConfig] = None,
               inference_log: Optional[MonitorInferenceLogProfileType] = None,
               notifications: Optional[List[MonitorNotificationsConfig]] = None,
               schedule: Optional[MonitorCronSchedule] = None,
               skip_builtin_dashboard: Optional[bool] = None,
               slicing_exprs: Optional[List[str]] = None,
               snapshot: Optional[MonitorSnapshotProfileType] = None,
               time_series: Optional[MonitorTimeSeriesProfileType] = None,
               warehouse_id: Optional[str] = None) -> MonitorInfo:
        """Create a table monitor.
        
        Creates a new monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog, have **USE_SCHEMA** on the
        table's parent schema, and have **SELECT** access on the table 2. have **USE_CATALOG** on the table's
        parent catalog, be an owner of the table's parent schema, and have **SELECT** access on the table. 3.
        have the following permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on
        the table's parent schema - be an owner of the table.
        
        Workspace assets, such as the dashboard, will be created in the workspace where this call was made.
        
        :param full_name: str
          Full name of the table.
        :param assets_dir: str
          The directory to store monitoring assets (e.g. dashboard, metric tables).
        :param output_schema_name: str
          Schema where output metric tables are created.
        :param baseline_table_name: str (optional)
          Name of the baseline table from which drift metrics are computed from. Columns in the monitored
          table should also be present in the baseline table.
        :param custom_metrics: List[:class:`MonitorCustomMetric`] (optional)
          Custom metrics to compute on the monitored table. These can be aggregate metrics, derived metrics
          (from already computed aggregate metrics), or drift metrics (comparing metrics across time windows).
        :param data_classification_config: :class:`MonitorDataClassificationConfig` (optional)
          The data classification config for the monitor.
        :param inference_log: :class:`MonitorInferenceLogProfileType` (optional)
          Configuration for monitoring inference logs.
        :param notifications: List[:class:`MonitorNotificationsConfig`] (optional)
          The notification settings for the monitor.
        :param schedule: :class:`MonitorCronSchedule` (optional)
          The schedule for automatically updating and refreshing metric tables.
        :param skip_builtin_dashboard: bool (optional)
          Whether to skip creating a default dashboard summarizing data quality metrics.
        :param slicing_exprs: List[str] (optional)
          List of column expressions to slice data with for targeted analysis. The data is grouped by each
          expression independently, resulting in a separate slice for each predicate and its complements. For
          high-cardinality columns, only the top 100 unique values by frequency will generate slices.
        :param snapshot: :class:`MonitorSnapshotProfileType` (optional)
          Configuration for monitoring snapshot tables.
        :param time_series: :class:`MonitorTimeSeriesProfileType` (optional)
          Configuration for monitoring time series tables.
        :param warehouse_id: str (optional)
          Optional argument to specify the warehouse for dashboard creation. If not specified, the first
          running warehouse will be used.
        
        :returns: :class:`MonitorInfo`
        """
        body = {}
        if assets_dir is not None: body['assets_dir'] = assets_dir
        if baseline_table_name is not None: body['baseline_table_name'] = baseline_table_name
        if custom_metrics is not None: body['custom_metrics'] = [v.as_dict() for v in custom_metrics]
        if data_classification_config is not None:
            body['data_classification_config'] = data_classification_config.as_dict()
        if inference_log is not None: body['inference_log'] = inference_log.as_dict()
        if notifications is not None: body['notifications'] = [v.as_dict() for v in notifications]
        if output_schema_name is not None: body['output_schema_name'] = output_schema_name
        if schedule is not None: body['schedule'] = schedule.as_dict()
        if skip_builtin_dashboard is not None: body['skip_builtin_dashboard'] = skip_builtin_dashboard
        if slicing_exprs is not None: body['slicing_exprs'] = [v for v in slicing_exprs]
        if snapshot is not None: body['snapshot'] = snapshot
        if time_series is not None: body['time_series'] = time_series.as_dict()
        if warehouse_id is not None: body['warehouse_id'] = warehouse_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.1/unity-catalog/tables/{full_name}/monitor',
                           body=body,
                           headers=headers)
        return MonitorInfo.from_dict(res)

    def delete(self, full_name: str):
        """Delete a table monitor.
        
        Deletes a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        Note that the metric tables and dashboard will not be deleted as part of this call; those assets must
        be manually cleaned up (if desired).
        
        :param full_name: str
          Full name of the table.
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.1/unity-catalog/tables/{full_name}/monitor', headers=headers)

    def get(self, full_name: str) -> MonitorInfo:
        """Get a table monitor.
        
        Gets a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema. 3. have the following
        permissions: - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent
        schema - **SELECT** privilege on the table.
        
        The returned information includes configuration values, as well as information on assets created by
        the monitor. Some information (e.g., dashboard) may be filtered out if the caller is in a different
        workspace than where the monitor was created.
        
        :param full_name: str
          Full name of the table.
        
        :returns: :class:`MonitorInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/tables/{full_name}/monitor', headers=headers)
        return MonitorInfo.from_dict(res)

    def get_refresh(self, full_name: str, refresh_id: str) -> MonitorRefreshInfo:
        """Get refresh.
        
        Gets info about a specific monitor refresh using the given refresh ID.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema -
        **SELECT** privilege on the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param full_name: str
          Full name of the table.
        :param refresh_id: str
          ID of the refresh.
        
        :returns: :class:`MonitorRefreshInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/tables/{full_name}/monitor/refreshes/{refresh_id}',
                           headers=headers)
        return MonitorRefreshInfo.from_dict(res)

    def list_refreshes(self, full_name: str) -> Iterator[MonitorRefreshInfo]:
        """List refreshes.
        
        Gets an array containing the history of the most recent refreshes (up to 25) for this table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema -
        **SELECT** privilege on the table.
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param full_name: str
          Full name of the table.
        
        :returns: Iterator over :class:`MonitorRefreshInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/tables/{full_name}/monitor/refreshes',
                           headers=headers)
        return [MonitorRefreshInfo.from_dict(v) for v in res]

    def run_refresh(self, full_name: str) -> MonitorRefreshInfo:
        """Queue a metric refresh for a monitor.
        
        Queues a metric refresh on the monitor for the specified table. The refresh will execute in the
        background.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table
        
        Additionally, the call must be made from the workspace where the monitor was created.
        
        :param full_name: str
          Full name of the table.
        
        :returns: :class:`MonitorRefreshInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('POST',
                           f'/api/2.1/unity-catalog/tables/{full_name}/monitor/refreshes',
                           headers=headers)
        return MonitorRefreshInfo.from_dict(res)

    def update(self,
               full_name: str,
               output_schema_name: str,
               *,
               baseline_table_name: Optional[str] = None,
               custom_metrics: Optional[List[MonitorCustomMetric]] = None,
               data_classification_config: Optional[MonitorDataClassificationConfig] = None,
               inference_log: Optional[MonitorInferenceLogProfileType] = None,
               notifications: Optional[List[MonitorNotificationsConfig]] = None,
               schedule: Optional[MonitorCronSchedule] = None,
               slicing_exprs: Optional[List[str]] = None,
               snapshot: Optional[MonitorSnapshotProfileType] = None,
               time_series: Optional[MonitorTimeSeriesProfileType] = None) -> MonitorInfo:
        """Update a table monitor.
        
        Updates a monitor for the specified table.
        
        The caller must either: 1. be an owner of the table's parent catalog 2. have **USE_CATALOG** on the
        table's parent catalog and be an owner of the table's parent schema 3. have the following permissions:
        - **USE_CATALOG** on the table's parent catalog - **USE_SCHEMA** on the table's parent schema - be an
        owner of the table.
        
        Additionally, the call must be made from the workspace where the monitor was created, and the caller
        must be the original creator of the monitor.
        
        Certain configuration fields, such as output asset identifiers, cannot be updated.
        
        :param full_name: str
          Full name of the table.
        :param output_schema_name: str
          Schema where output metric tables are created.
        :param baseline_table_name: str (optional)
          Name of the baseline table from which drift metrics are computed from. Columns in the monitored
          table should also be present in the baseline table.
        :param custom_metrics: List[:class:`MonitorCustomMetric`] (optional)
          Custom metrics to compute on the monitored table. These can be aggregate metrics, derived metrics
          (from already computed aggregate metrics), or drift metrics (comparing metrics across time windows).
        :param data_classification_config: :class:`MonitorDataClassificationConfig` (optional)
          The data classification config for the monitor.
        :param inference_log: :class:`MonitorInferenceLogProfileType` (optional)
          Configuration for monitoring inference logs.
        :param notifications: List[:class:`MonitorNotificationsConfig`] (optional)
          The notification settings for the monitor.
        :param schedule: :class:`MonitorCronSchedule` (optional)
          The schedule for automatically updating and refreshing metric tables.
        :param slicing_exprs: List[str] (optional)
          List of column expressions to slice data with for targeted analysis. The data is grouped by each
          expression independently, resulting in a separate slice for each predicate and its complements. For
          high-cardinality columns, only the top 100 unique values by frequency will generate slices.
        :param snapshot: :class:`MonitorSnapshotProfileType` (optional)
          Configuration for monitoring snapshot tables.
        :param time_series: :class:`MonitorTimeSeriesProfileType` (optional)
          Configuration for monitoring time series tables.
        
        :returns: :class:`MonitorInfo`
        """
        body = {}
        if baseline_table_name is not None: body['baseline_table_name'] = baseline_table_name
        if custom_metrics is not None: body['custom_metrics'] = [v.as_dict() for v in custom_metrics]
        if data_classification_config is not None:
            body['data_classification_config'] = data_classification_config.as_dict()
        if inference_log is not None: body['inference_log'] = inference_log.as_dict()
        if notifications is not None: body['notifications'] = [v.as_dict() for v in notifications]
        if output_schema_name is not None: body['output_schema_name'] = output_schema_name
        if schedule is not None: body['schedule'] = schedule.as_dict()
        if slicing_exprs is not None: body['slicing_exprs'] = [v for v in slicing_exprs]
        if snapshot is not None: body['snapshot'] = snapshot
        if time_series is not None: body['time_series'] = time_series.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.1/unity-catalog/tables/{full_name}/monitor',
                           body=body,
                           headers=headers)
        return MonitorInfo.from_dict(res)


class MetastoresAPI:
    """A metastore is the top-level container of objects in Unity Catalog. It stores data assets (tables and
    views) and the permissions that govern access to them. Databricks account admins can create metastores and
    assign them to Databricks workspaces to control which workloads use each metastore. For a workspace to use
    Unity Catalog, it must have a Unity Catalog metastore attached.
    
    Each metastore is configured with a root storage location in a cloud storage account. This storage
    location is used for metadata and managed tables data.
    
    NOTE: This metastore is distinct from the metastore included in Databricks workspaces created before Unity
    Catalog was released. If your workspace includes a legacy Hive metastore, the data in that metastore is
    available in a catalog named hive_metastore."""

    def __init__(self, api_client):
        self._api = api_client

    def assign(self, workspace_id: int, metastore_id: str, default_catalog_name: str):
        """Create an assignment.
        
        Creates a new metastore assignment. If an assignment for the same __workspace_id__ exists, it will be
        overwritten by the new __metastore_id__ and __default_catalog_name__. The caller must be an account
        admin.
        
        :param workspace_id: int
          A workspace ID.
        :param metastore_id: str
          The unique ID of the metastore.
        :param default_catalog_name: str
          The name of the default catalog in the metastore.
        
        
        """
        body = {}
        if default_catalog_name is not None: body['default_catalog_name'] = default_catalog_name
        if metastore_id is not None: body['metastore_id'] = metastore_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PUT',
                     f'/api/2.1/unity-catalog/workspaces/{workspace_id}/metastore',
                     body=body,
                     headers=headers)

    def create(self,
               name: str,
               *,
               region: Optional[str] = None,
               storage_root: Optional[str] = None) -> MetastoreInfo:
        """Create a metastore.
        
        Creates a new metastore based on a provided name and optional storage root path. By default (if the
        __owner__ field is not set), the owner of the new metastore is the user calling the
        __createMetastore__ API. If the __owner__ field is set to the empty string (**""**), the ownership is
        assigned to the System User instead.
        
        :param name: str
          The user-specified name of the metastore.
        :param region: str (optional)
          Cloud region which the metastore serves (e.g., `us-west-2`, `westus`). If this field is omitted, the
          region of the workspace receiving the request will be used.
        :param storage_root: str (optional)
          The storage root URL for metastore
        
        :returns: :class:`MetastoreInfo`
        """
        body = {}
        if name is not None: body['name'] = name
        if region is not None: body['region'] = region
        if storage_root is not None: body['storage_root'] = storage_root
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/metastores', body=body, headers=headers)
        return MetastoreInfo.from_dict(res)

    def current(self) -> MetastoreAssignment:
        """Get metastore assignment for workspace.
        
        Gets the metastore assignment for the workspace being accessed.
        
        :returns: :class:`MetastoreAssignment`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', '/api/2.1/unity-catalog/current-metastore-assignment', headers=headers)
        return MetastoreAssignment.from_dict(res)

    def delete(self, id: str, *, force: Optional[bool] = None):
        """Delete a metastore.
        
        Deletes a metastore. The caller must be a metastore admin.
        
        :param id: str
          Unique ID of the metastore.
        :param force: bool (optional)
          Force deletion even if the metastore is not empty. Default is false.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/metastores/{id}', query=query, headers=headers)

    def get(self, id: str) -> MetastoreInfo:
        """Get a metastore.
        
        Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this
        info.
        
        :param id: str
          Unique ID of the metastore.
        
        :returns: :class:`MetastoreInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/metastores/{id}', headers=headers)
        return MetastoreInfo.from_dict(res)

    def list(self) -> Iterator[MetastoreInfo]:
        """List metastores.
        
        Gets an array of the available metastores (as __MetastoreInfo__ objects). The caller must be an admin
        to retrieve this info. There is no guarantee of a specific ordering of the elements in the array.
        
        :returns: Iterator over :class:`MetastoreInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.1/unity-catalog/metastores', headers=headers)
        parsed = ListMetastoresResponse.from_dict(json).metastores
        return parsed if parsed is not None else []

    def summary(self) -> GetMetastoreSummaryResponse:
        """Get a metastore summary.
        
        Gets information about a metastore. This summary includes the storage credential, the cloud vendor,
        the cloud region, and the global metastore ID.
        
        :returns: :class:`GetMetastoreSummaryResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', '/api/2.1/unity-catalog/metastore_summary', headers=headers)
        return GetMetastoreSummaryResponse.from_dict(res)

    def unassign(self, workspace_id: int, metastore_id: str):
        """Delete an assignment.
        
        Deletes a metastore assignment. The caller must be an account administrator.
        
        :param workspace_id: int
          A workspace ID.
        :param metastore_id: str
          Query for the ID of the metastore to delete.
        
        
        """

        query = {}
        if metastore_id is not None: query['metastore_id'] = metastore_id
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/workspaces/{workspace_id}/metastore',
                     query=query,
                     headers=headers)

    def update(self,
               id: str,
               *,
               delta_sharing_organization_name: Optional[str] = None,
               delta_sharing_recipient_token_lifetime_in_seconds: Optional[int] = None,
               delta_sharing_scope: Optional[UpdateMetastoreDeltaSharingScope] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None,
               privilege_model_version: Optional[str] = None,
               storage_root_credential_id: Optional[str] = None) -> MetastoreInfo:
        """Update a metastore.
        
        Updates information for a specific metastore. The caller must be a metastore admin. If the __owner__
        field is set to the empty string (**""**), the ownership is updated to the System User.
        
        :param id: str
          Unique ID of the metastore.
        :param delta_sharing_organization_name: str (optional)
          The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta
          Sharing as the official name.
        :param delta_sharing_recipient_token_lifetime_in_seconds: int (optional)
          The lifetime of delta sharing recipient token in seconds.
        :param delta_sharing_scope: :class:`UpdateMetastoreDeltaSharingScope` (optional)
          The scope of Delta Sharing enabled for the metastore.
        :param new_name: str (optional)
          New name for the metastore.
        :param owner: str (optional)
          The owner of the metastore.
        :param privilege_model_version: str (optional)
          Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`).
        :param storage_root_credential_id: str (optional)
          UUID of storage credential to access the metastore storage_root.
        
        :returns: :class:`MetastoreInfo`
        """
        body = {}
        if delta_sharing_organization_name is not None:
            body['delta_sharing_organization_name'] = delta_sharing_organization_name
        if delta_sharing_recipient_token_lifetime_in_seconds is not None:
            body[
                'delta_sharing_recipient_token_lifetime_in_seconds'] = delta_sharing_recipient_token_lifetime_in_seconds
        if delta_sharing_scope is not None: body['delta_sharing_scope'] = delta_sharing_scope.value
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        if privilege_model_version is not None: body['privilege_model_version'] = privilege_model_version
        if storage_root_credential_id is not None:
            body['storage_root_credential_id'] = storage_root_credential_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/metastores/{id}', body=body, headers=headers)
        return MetastoreInfo.from_dict(res)

    def update_assignment(self,
                          workspace_id: int,
                          *,
                          default_catalog_name: Optional[str] = None,
                          metastore_id: Optional[str] = None):
        """Update an assignment.
        
        Updates a metastore assignment. This operation can be used to update __metastore_id__ or
        __default_catalog_name__ for a specified Workspace, if the Workspace is already assigned a metastore.
        The caller must be an account admin to update __metastore_id__; otherwise, the caller can be a
        Workspace admin.
        
        :param workspace_id: int
          A workspace ID.
        :param default_catalog_name: str (optional)
          The name of the default catalog for the metastore.
        :param metastore_id: str (optional)
          The unique ID of the metastore.
        
        
        """
        body = {}
        if default_catalog_name is not None: body['default_catalog_name'] = default_catalog_name
        if metastore_id is not None: body['metastore_id'] = metastore_id
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH',
                     f'/api/2.1/unity-catalog/workspaces/{workspace_id}/metastore',
                     body=body,
                     headers=headers)


class ModelVersionsAPI:
    """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in Unity Catalog
    provide centralized access control, auditing, lineage, and discovery of ML models across Databricks
    workspaces.
    
    This API reference documents the REST endpoints for managing model versions in Unity Catalog. For more
    details, see the [registered models API docs](/api/workspace/registeredmodels)."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, full_name: str, version: int):
        """Delete a Model Version.
        
        Deletes a model version from the specified registered model. Any aliases assigned to the model version
        will also be deleted.
        
        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        
        
        """

        headers = {}

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/models/{full_name}/versions/{version}',
                     headers=headers)

    def get(self, full_name: str, version: int) -> RegisteredModelInfo:
        """Get a Model Version.
        
        Get a model version.
        
        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the parent
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        
        :returns: :class:`RegisteredModelInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/models/{full_name}/versions/{version}',
                           headers=headers)
        return RegisteredModelInfo.from_dict(res)

    def get_by_alias(self, full_name: str, alias: str) -> ModelVersionInfo:
        """Get Model Version By Alias.
        
        Get a model version by alias.
        
        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param alias: str
          The name of the alias
        
        :returns: :class:`ModelVersionInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/models/{full_name}/aliases/{alias}',
                           headers=headers)
        return ModelVersionInfo.from_dict(res)

    def list(self,
             full_name: str,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[ModelVersionInfo]:
        """List Model Versions.
        
        List model versions. You can list model versions under a particular schema, or list all model versions
        in the current metastore.
        
        The returned models are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the model versions. A regular user needs to be the owner or have
        the **EXECUTE** privilege on the parent registered model to recieve the model versions in the
        response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the response.
        
        :param full_name: str
          The full three-level name of the registered model under which to list model versions
        :param max_results: int (optional)
          Maximum number of model versions to return. If not set, the page length is set to a server
          configured value (100, as of 1/3/2024). - when set to a value greater than 0, the page length is the
          minimum of this value and a server configured value(1000, as of 1/3/2024); - when set to 0, the page
          length is set to a server configured value (100, as of 1/3/2024) (recommended); - when set to a
          value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`ModelVersionInfo`
        """

        query = {}
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                f'/api/2.1/unity-catalog/models/{full_name}/versions',
                                query=query,
                                headers=headers)
            if 'model_versions' in json:
                for v in json['model_versions']:
                    yield ModelVersionInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self, full_name: str, version: int, *, comment: Optional[str] = None) -> ModelVersionInfo:
        """Update a Model Version.
        
        Updates the specified model version.
        
        The caller must be a metastore admin or an owner of the parent registered model. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        Currently only the comment of the model version can be updated.
        
        :param full_name: str
          The three-level (fully qualified) name of the model version
        :param version: int
          The integer version number of the model version
        :param comment: str (optional)
          The comment attached to the model version
        
        :returns: :class:`ModelVersionInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/models/{full_name}/versions/{version}',
                           body=body,
                           headers=headers)
        return ModelVersionInfo.from_dict(res)


class OnlineTablesAPI:
    """Online tables provide lower latency and higher QPS access to data from Delta tables."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, *, name: Optional[str] = None, spec: Optional[OnlineTableSpec] = None) -> OnlineTable:
        """Create an Online Table.
        
        Create a new Online Table.
        
        :param name: str (optional)
          Full three-part (catalog, schema, table) name of the table.
        :param spec: :class:`OnlineTableSpec` (optional)
          Specification of the online table.
        
        :returns: :class:`OnlineTable`
        """
        body = {}
        if name is not None: body['name'] = name
        if spec is not None: body['spec'] = spec.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.0/online-tables', body=body, headers=headers)
        return OnlineTable.from_dict(res)

    def delete(self, name: str):
        """Delete an Online Table.
        
        Delete an online table. Warning: This will delete all the data in the online table. If the source
        Delta table was deleted or modified since this Online Table was created, this will lose the data
        forever!
        
        :param name: str
          Full three-part (catalog, schema, table) name of the table.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/online-tables/{name}', headers=headers)

    def get(self, name: str) -> OnlineTable:
        """Get an Online Table.
        
        Get information about an existing online table and its status.
        
        :param name: str
          Full three-part (catalog, schema, table) name of the table.
        
        :returns: :class:`OnlineTable`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/online-tables/{name}', headers=headers)
        return OnlineTable.from_dict(res)


class RegisteredModelsAPI:
    """Databricks provides a hosted version of MLflow Model Registry in Unity Catalog. Models in Unity Catalog
    provide centralized access control, auditing, lineage, and discovery of ML models across Databricks
    workspaces.
    
    An MLflow registered model resides in the third layer of Unity Catalog’s three-level namespace.
    Registered models contain model versions, which correspond to actual ML models (MLflow models). Creating
    new model versions currently requires use of the MLflow Python client. Once model versions are created,
    you can load them for batch inference using MLflow Python client APIs, or deploy them for real-time
    serving using Databricks Model Serving.
    
    All operations on registered models and model versions require USE_CATALOG permissions on the enclosing
    catalog and USE_SCHEMA permissions on the enclosing schema. In addition, the following additional
    privileges are required for various operations:
    
    * To create a registered model, users must additionally have the CREATE_MODEL permission on the target
    schema. * To view registered model or model version metadata, model version data files, or invoke a model
    version, users must additionally have the EXECUTE permission on the registered model * To update
    registered model or model version tags, users must additionally have APPLY TAG permissions on the
    registered model * To update other registered model or model version metadata (comments, aliases) create a
    new model version, or update permissions on the registered model, users must be owners of the registered
    model.
    
    Note: The securable type for models is "FUNCTION". When using REST APIs (e.g. tagging, grants) that
    specify a securable type, use "FUNCTION" as the securable type."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               catalog_name: str,
               schema_name: str,
               name: str,
               *,
               comment: Optional[str] = None,
               storage_location: Optional[str] = None) -> RegisteredModelInfo:
        """Create a Registered Model.
        
        Creates a new registered model in Unity Catalog.
        
        File storage for model versions in the registered model will be located in the default location which
        is specified by the parent schema, or the parent catalog, or the Metastore.
        
        For registered model creation to succeed, the user must satisfy the following conditions: - The caller
        must be a metastore admin, or be the owner of the parent catalog and schema, or have the
        **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        - The caller must have the **CREATE MODEL** or **CREATE FUNCTION** privilege on the parent schema.
        
        :param catalog_name: str
          The name of the catalog where the schema and the registered model reside
        :param schema_name: str
          The name of the schema where the registered model resides
        :param name: str
          The name of the registered model
        :param comment: str (optional)
          The comment attached to the registered model
        :param storage_location: str (optional)
          The storage location on the cloud under which model version data files are stored
        
        :returns: :class:`RegisteredModelInfo`
        """
        body = {}
        if catalog_name is not None: body['catalog_name'] = catalog_name
        if comment is not None: body['comment'] = comment
        if name is not None: body['name'] = name
        if schema_name is not None: body['schema_name'] = schema_name
        if storage_location is not None: body['storage_location'] = storage_location
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/models', body=body, headers=headers)
        return RegisteredModelInfo.from_dict(res)

    def delete(self, full_name: str):
        """Delete a Registered Model.
        
        Deletes a registered model and all its model versions from the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.1/unity-catalog/models/{full_name}', headers=headers)

    def delete_alias(self, full_name: str, alias: str):
        """Delete a Registered Model Alias.
        
        Deletes a registered model alias.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param alias: str
          The name of the alias
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.1/unity-catalog/models/{full_name}/aliases/{alias}', headers=headers)

    def get(self, full_name: str) -> RegisteredModelInfo:
        """Get a Registered Model.
        
        Get a registered model.
        
        The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the
        registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        
        :returns: :class:`RegisteredModelInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/models/{full_name}', headers=headers)
        return RegisteredModelInfo.from_dict(res)

    def list(self,
             *,
             catalog_name: Optional[str] = None,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None,
             schema_name: Optional[str] = None) -> Iterator[RegisteredModelInfo]:
        """List Registered Models.
        
        List registered models. You can list registered models under a particular schema, or list all
        registered models in the current metastore.
        
        The returned models are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the registered models. A regular user needs to be the owner or
        have the **EXECUTE** privilege on the registered model to recieve the registered models in the
        response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the response.
        
        :param catalog_name: str (optional)
          The identifier of the catalog under which to list registered models. If specified, schema_name must
          be specified.
        :param max_results: int (optional)
          Max number of registered models to return. If catalog and schema are unspecified, max_results must
          be specified. If max_results is unspecified, we return all results, starting from the page specified
          by page_token.
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        :param schema_name: str (optional)
          The identifier of the schema under which to list registered models. If specified, catalog_name must
          be specified.
        
        :returns: Iterator over :class:`RegisteredModelInfo`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        if schema_name is not None: query['schema_name'] = schema_name
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/models', query=query, headers=headers)
            if 'registered_models' in json:
                for v in json['registered_models']:
                    yield RegisteredModelInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def set_alias(self, full_name: str, alias: str, version_num: int) -> RegisteredModelAlias:
        """Set a Registered Model Alias.
        
        Set an alias on the specified registered model.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          Full name of the registered model
        :param alias: str
          The name of the alias
        :param version_num: int
          The version number of the model version to which the alias points
        
        :returns: :class:`RegisteredModelAlias`
        """
        body = {}
        if version_num is not None: body['version_num'] = version_num
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.1/unity-catalog/models/{full_name}/aliases/{alias}',
                           body=body,
                           headers=headers)
        return RegisteredModelAlias.from_dict(res)

    def update(self,
               full_name: str,
               *,
               comment: Optional[str] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None) -> RegisteredModelInfo:
        """Update a Registered Model.
        
        Updates the specified registered model.
        
        The caller must be a metastore admin or an owner of the registered model. For the latter case, the
        caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        Currently only the name, the owner or the comment of the registered model can be updated.
        
        :param full_name: str
          The three-level (fully qualified) name of the registered model
        :param comment: str (optional)
          The comment attached to the registered model
        :param new_name: str (optional)
          New name for the registered model.
        :param owner: str (optional)
          The identifier of the user who owns the registered model
        
        :returns: :class:`RegisteredModelInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/models/{full_name}', body=body, headers=headers)
        return RegisteredModelInfo.from_dict(res)


class SchemasAPI:
    """A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace. A schema
    organizes tables, views and functions. To access (or list) a table or view in a schema, users must have
    the USE_SCHEMA data permission on the schema and its parent catalog, and they must have the SELECT
    permission on the table or view."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               catalog_name: str,
               *,
               comment: Optional[str] = None,
               properties: Optional[Dict[str, str]] = None,
               storage_root: Optional[str] = None) -> SchemaInfo:
        """Create a schema.
        
        Creates a new schema for catalog in the Metatastore. The caller must be a metastore admin, or have the
        **CREATE_SCHEMA** privilege in the parent catalog.
        
        :param name: str
          Name of schema, relative to parent catalog.
        :param catalog_name: str
          Name of parent catalog.
        :param comment: str (optional)
          User-provided free-form text description.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param storage_root: str (optional)
          Storage root URL for managed tables within schema.
        
        :returns: :class:`SchemaInfo`
        """
        body = {}
        if catalog_name is not None: body['catalog_name'] = catalog_name
        if comment is not None: body['comment'] = comment
        if name is not None: body['name'] = name
        if properties is not None: body['properties'] = properties
        if storage_root is not None: body['storage_root'] = storage_root
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/schemas', body=body, headers=headers)
        return SchemaInfo.from_dict(res)

    def delete(self, full_name: str):
        """Delete a schema.
        
        Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an
        owner of the parent catalog.
        
        :param full_name: str
          Full name of the schema.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/schemas/{full_name}', headers=headers)

    def get(self, full_name: str) -> SchemaInfo:
        """Get a schema.
        
        Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the
        schema, or a user that has the **USE_SCHEMA** privilege on the schema.
        
        :param full_name: str
          Full name of the schema.
        
        :returns: :class:`SchemaInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/schemas/{full_name}', headers=headers)
        return SchemaInfo.from_dict(res)

    def list(self,
             catalog_name: str,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[SchemaInfo]:
        """List schemas.
        
        Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the
        owner of the parent catalog, all schemas for the catalog will be retrieved. Otherwise, only schemas
        owned by the caller (or for which the caller has the **USE_SCHEMA** privilege) will be retrieved. For
        unpaginated request, there is no guarantee of a specific ordering of the elements in the array. For
        paginated request, elements are ordered by their name.
        
        :param catalog_name: str
          Parent catalog for schemas of interest.
        :param max_results: int (optional)
          Maximum number of schemas to return. If not set, all the schemas are returned (not recommended). -
          when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`SchemaInfo`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/schemas', query=query, headers=headers)
            if 'schemas' in json:
                for v in json['schemas']:
                    yield SchemaInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self,
               full_name: str,
               *,
               comment: Optional[str] = None,
               enable_predictive_optimization: Optional[EnablePredictiveOptimization] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None,
               properties: Optional[Dict[str, str]] = None) -> SchemaInfo:
        """Update a schema.
        
        Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If
        the caller is a metastore admin, only the __owner__ field can be changed in the update. If the
        __name__ field must be updated, the caller must be a metastore admin or have the **CREATE_SCHEMA**
        privilege on the parent catalog.
        
        :param full_name: str
          Full name of the schema.
        :param comment: str (optional)
          User-provided free-form text description.
        :param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)
          Whether predictive optimization should be enabled for this object and objects under it.
        :param new_name: str (optional)
          New name for the schema.
        :param owner: str (optional)
          Username of current owner of schema.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        
        :returns: :class:`SchemaInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if enable_predictive_optimization is not None:
            body['enable_predictive_optimization'] = enable_predictive_optimization.value
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        if properties is not None: body['properties'] = properties
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/schemas/{full_name}', body=body, headers=headers)
        return SchemaInfo.from_dict(res)


class StorageCredentialsAPI:
    """A storage credential represents an authentication and authorization mechanism for accessing data stored on
    your cloud tenant. Each storage credential is subject to Unity Catalog access-control policies that
    control which users and groups can access the credential. If a user does not have access to a storage
    credential in Unity Catalog, the request fails and Unity Catalog does not attempt to authenticate to your
    cloud tenant on the user’s behalf.
    
    Databricks recommends using external locations rather than using storage credentials directly.
    
    To create storage credentials, you must be a Databricks account admin. The account admin who creates the
    storage credential can delegate ownership to another user or group to manage permissions on it."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               name: str,
               *,
               aws_iam_role: Optional[AwsIamRole] = None,
               azure_managed_identity: Optional[AzureManagedIdentity] = None,
               azure_service_principal: Optional[AzureServicePrincipal] = None,
               cloudflare_api_token: Optional[CloudflareApiToken] = None,
               comment: Optional[str] = None,
               databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None,
               read_only: Optional[bool] = None,
               skip_validation: Optional[bool] = None) -> StorageCredentialInfo:
        """Create a storage credential.
        
        Creates a new storage credential.
        
        :param name: str
          The credential name. The name must be unique within the metastore.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The <Databricks> managed GCP service account configuration.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the created credential.
        
        :returns: :class:`StorageCredentialInfo`
        """
        body = {}
        if aws_iam_role is not None: body['aws_iam_role'] = aws_iam_role.as_dict()
        if azure_managed_identity is not None:
            body['azure_managed_identity'] = azure_managed_identity.as_dict()
        if azure_service_principal is not None:
            body['azure_service_principal'] = azure_service_principal.as_dict()
        if cloudflare_api_token is not None: body['cloudflare_api_token'] = cloudflare_api_token.as_dict()
        if comment is not None: body['comment'] = comment
        if databricks_gcp_service_account is not None:
            body['databricks_gcp_service_account'] = databricks_gcp_service_account
        if name is not None: body['name'] = name
        if read_only is not None: body['read_only'] = read_only
        if skip_validation is not None: body['skip_validation'] = skip_validation
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/storage-credentials', body=body, headers=headers)
        return StorageCredentialInfo.from_dict(res)

    def delete(self, name: str, *, force: Optional[bool] = None):
        """Delete a credential.
        
        Deletes a storage credential from the metastore. The caller must be an owner of the storage
        credential.
        
        :param name: str
          Name of the storage credential.
        :param force: bool (optional)
          Force deletion even if there are dependent external locations or external tables.
        
        
        """

        query = {}
        if force is not None: query['force'] = force
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/storage-credentials/{name}',
                     query=query,
                     headers=headers)

    def get(self, name: str) -> StorageCredentialInfo:
        """Get a credential.
        
        Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the
        storage credential, or have some permission on the storage credential.
        
        :param name: str
          Name of the storage credential.
        
        :returns: :class:`StorageCredentialInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/storage-credentials/{name}', headers=headers)
        return StorageCredentialInfo.from_dict(res)

    def list(self,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[StorageCredentialInfo]:
        """List credentials.
        
        Gets an array of storage credentials (as __StorageCredentialInfo__ objects). The array is limited to
        only those storage credentials the caller has permission to access. If the caller is a metastore
        admin, retrieval of credentials is unrestricted. For unpaginated request, there is no guarantee of a
        specific ordering of the elements in the array. For paginated request, elements are ordered by their
        name.
        
        :param max_results: int (optional)
          Maximum number of storage credentials to return. If not set, all the storage credentials are
          returned (not recommended). - when set to a value greater than 0, the page length is the minimum of
          this value and a server configured value; - when set to 0, the page length is set to a server
          configured value (recommended); - when set to a value less than 0, an invalid parameter error is
          returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`StorageCredentialInfo`
        """

        query = {}
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET',
                                '/api/2.1/unity-catalog/storage-credentials',
                                query=query,
                                headers=headers)
            if 'storage_credentials' in json:
                for v in json['storage_credentials']:
                    yield StorageCredentialInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self,
               name: str,
               *,
               aws_iam_role: Optional[AwsIamRole] = None,
               azure_managed_identity: Optional[AzureManagedIdentity] = None,
               azure_service_principal: Optional[AzureServicePrincipal] = None,
               cloudflare_api_token: Optional[CloudflareApiToken] = None,
               comment: Optional[str] = None,
               databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None,
               force: Optional[bool] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None,
               read_only: Optional[bool] = None,
               skip_validation: Optional[bool] = None) -> StorageCredentialInfo:
        """Update a credential.
        
        Updates a storage credential on the metastore.
        
        :param name: str
          Name of the storage credential.
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param comment: str (optional)
          Comment associated with the credential.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The <Databricks> managed GCP service account configuration.
        :param force: bool (optional)
          Force update even if there are dependent external locations or external tables.
        :param new_name: str (optional)
          New name for the storage credential.
        :param owner: str (optional)
          Username of current owner of credential.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param skip_validation: bool (optional)
          Supplying true to this argument skips validation of the updated credential.
        
        :returns: :class:`StorageCredentialInfo`
        """
        body = {}
        if aws_iam_role is not None: body['aws_iam_role'] = aws_iam_role.as_dict()
        if azure_managed_identity is not None:
            body['azure_managed_identity'] = azure_managed_identity.as_dict()
        if azure_service_principal is not None:
            body['azure_service_principal'] = azure_service_principal.as_dict()
        if cloudflare_api_token is not None: body['cloudflare_api_token'] = cloudflare_api_token.as_dict()
        if comment is not None: body['comment'] = comment
        if databricks_gcp_service_account is not None:
            body['databricks_gcp_service_account'] = databricks_gcp_service_account
        if force is not None: body['force'] = force
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        if read_only is not None: body['read_only'] = read_only
        if skip_validation is not None: body['skip_validation'] = skip_validation
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/storage-credentials/{name}',
                           body=body,
                           headers=headers)
        return StorageCredentialInfo.from_dict(res)

    def validate(self,
                 *,
                 aws_iam_role: Optional[AwsIamRole] = None,
                 azure_managed_identity: Optional[AzureManagedIdentity] = None,
                 azure_service_principal: Optional[AzureServicePrincipal] = None,
                 cloudflare_api_token: Optional[CloudflareApiToken] = None,
                 databricks_gcp_service_account: Optional[DatabricksGcpServiceAccountRequest] = None,
                 external_location_name: Optional[str] = None,
                 read_only: Optional[bool] = None,
                 storage_credential_name: Optional[str] = None,
                 url: Optional[str] = None) -> ValidateStorageCredentialResponse:
        """Validate a storage credential.
        
        Validates a storage credential. At least one of __external_location_name__ and __url__ need to be
        provided. If only one of them is provided, it will be used for validation. And if both are provided,
        the __url__ will be used for validation, and __external_location_name__ will be ignored when checking
        overlapping urls.
        
        Either the __storage_credential_name__ or the cloud-specific credential must be provided.
        
        The caller must be a metastore admin or the storage credential owner or have the
        **CREATE_EXTERNAL_LOCATION** privilege on the metastore and the storage credential.
        
        :param aws_iam_role: :class:`AwsIamRole` (optional)
          The AWS IAM role configuration.
        :param azure_managed_identity: :class:`AzureManagedIdentity` (optional)
          The Azure managed identity configuration.
        :param azure_service_principal: :class:`AzureServicePrincipal` (optional)
          The Azure service principal configuration.
        :param cloudflare_api_token: :class:`CloudflareApiToken` (optional)
          The Cloudflare API token configuration.
        :param databricks_gcp_service_account: :class:`DatabricksGcpServiceAccountRequest` (optional)
          The Databricks created GCP service account configuration.
        :param external_location_name: str (optional)
          The name of an existing external location to validate.
        :param read_only: bool (optional)
          Whether the storage credential is only usable for read operations.
        :param storage_credential_name: str (optional)
          The name of the storage credential to validate.
        :param url: str (optional)
          The external location url to validate.
        
        :returns: :class:`ValidateStorageCredentialResponse`
        """
        body = {}
        if aws_iam_role is not None: body['aws_iam_role'] = aws_iam_role.as_dict()
        if azure_managed_identity is not None:
            body['azure_managed_identity'] = azure_managed_identity.as_dict()
        if azure_service_principal is not None:
            body['azure_service_principal'] = azure_service_principal.as_dict()
        if cloudflare_api_token is not None: body['cloudflare_api_token'] = cloudflare_api_token.as_dict()
        if databricks_gcp_service_account is not None:
            body['databricks_gcp_service_account'] = databricks_gcp_service_account
        if external_location_name is not None: body['external_location_name'] = external_location_name
        if read_only is not None: body['read_only'] = read_only
        if storage_credential_name is not None: body['storage_credential_name'] = storage_credential_name
        if url is not None: body['url'] = url
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST',
                           '/api/2.1/unity-catalog/validate-storage-credentials',
                           body=body,
                           headers=headers)
        return ValidateStorageCredentialResponse.from_dict(res)


class SystemSchemasAPI:
    """A system schema is a schema that lives within the system catalog. A system schema may contain information
    about customer usage of Unity Catalog such as audit-logs, billing-logs, lineage information, etc."""

    def __init__(self, api_client):
        self._api = api_client

    def disable(self, metastore_id: str, schema_name: DisableSchemaName):
        """Disable a system schema.
        
        Disables the system schema and removes it from the system catalog. The caller must be an account admin
        or a metastore admin.
        
        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: :class:`DisableSchemaName`
          Full name of the system schema.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/metastores/{metastore_id}/systemschemas/{schema_name.value}',
                     headers=headers)

    def enable(self, metastore_id: str, schema_name: EnableSchemaName):
        """Enable a system schema.
        
        Enables the system schema and adds it to the system catalog. The caller must be an account admin or a
        metastore admin.
        
        :param metastore_id: str
          The metastore ID under which the system schema lives.
        :param schema_name: :class:`EnableSchemaName`
          Full name of the system schema.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('PUT',
                     f'/api/2.1/unity-catalog/metastores/{metastore_id}/systemschemas/{schema_name.value}',
                     headers=headers)

    def list(self, metastore_id: str) -> Iterator[SystemSchemaInfo]:
        """List system schemas.
        
        Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore
        admin.
        
        :param metastore_id: str
          The ID for the metastore in which the system schema resides.
        
        :returns: Iterator over :class:`SystemSchemaInfo`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET',
                            f'/api/2.1/unity-catalog/metastores/{metastore_id}/systemschemas',
                            headers=headers)
        parsed = ListSystemSchemasResponse.from_dict(json).schemas
        return parsed if parsed is not None else []


class TableConstraintsAPI:
    """Primary key and foreign key constraints encode relationships between fields in tables.
    
    Primary and foreign keys are informational only and are not enforced. Foreign keys must reference a
    primary key in another table. This primary key is the parent constraint of the foreign key and the table
    this primary key is on is the parent table of the foreign key. Similarly, the foreign key is the child
    constraint of its referenced primary key; the table of the foreign key is the child table of the primary
    key.
    
    You can declare primary keys and foreign keys as part of the table specification during table creation.
    You can also add or drop constraints on existing tables."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self, full_name_arg: str, constraint: TableConstraint) -> TableConstraint:
        """Create a table constraint.
        
        Creates a new table constraint.
        
        For the table constraint creation to succeed, the user must satisfy both of these conditions: - the
        user must have the **USE_CATALOG** privilege on the table's parent catalog, the **USE_SCHEMA**
        privilege on the table's parent schema, and be the owner of the table. - if the new constraint is a
        __ForeignKeyConstraint__, the user must have the **USE_CATALOG** privilege on the referenced parent
        table's catalog, the **USE_SCHEMA** privilege on the referenced parent table's schema, and be the
        owner of the referenced parent table.
        
        :param full_name_arg: str
          The full name of the table referenced by the constraint.
        :param constraint: :class:`TableConstraint`
          A table constraint, as defined by *one* of the following fields being set:
          __primary_key_constraint__, __foreign_key_constraint__, __named_table_constraint__.
        
        :returns: :class:`TableConstraint`
        """
        body = {}
        if constraint is not None: body['constraint'] = constraint.as_dict()
        if full_name_arg is not None: body['full_name_arg'] = full_name_arg
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/constraints', body=body, headers=headers)
        return TableConstraint.from_dict(res)

    def delete(self, full_name: str, constraint_name: str, cascade: bool):
        """Delete a table constraint.
        
        Deletes a table constraint.
        
        For the table constraint deletion to succeed, the user must satisfy both of these conditions: - the
        user must have the **USE_CATALOG** privilege on the table's parent catalog, the **USE_SCHEMA**
        privilege on the table's parent schema, and be the owner of the table. - if __cascade__ argument is
        **true**, the user must have the following permissions on all of the child tables: the **USE_CATALOG**
        privilege on the table's catalog, the **USE_SCHEMA** privilege on the table's schema, and be the owner
        of the table.
        
        :param full_name: str
          Full name of the table referenced by the constraint.
        :param constraint_name: str
          The name of the constraint to delete.
        :param cascade: bool
          If true, try deleting all child constraints of the current constraint. If false, reject this
          operation if the current constraint has any child constraints.
        
        
        """

        query = {}
        if cascade is not None: query['cascade'] = cascade
        if constraint_name is not None: query['constraint_name'] = constraint_name
        headers = {'Accept': 'application/json', }

        self._api.do('DELETE',
                     f'/api/2.1/unity-catalog/constraints/{full_name}',
                     query=query,
                     headers=headers)


class TablesAPI:
    """A table resides in the third layer of Unity Catalog’s three-level namespace. It contains rows of data.
    To create a table, users must have CREATE_TABLE and USE_SCHEMA permissions on the schema, and they must
    have the USE_CATALOG permission on its parent catalog. To query a table, users must have the SELECT
    permission on the table, and they must have the USE_CATALOG permission on its parent catalog and the
    USE_SCHEMA permission on its parent schema.
    
    A table can be managed or external. From an API perspective, a __VIEW__ is a particular kind of table
    (rather than a managed or external table)."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, full_name: str):
        """Delete a table.
        
        Deletes a table from the specified parent catalog and schema. The caller must be the owner of the
        parent catalog, have the **USE_CATALOG** privilege on the parent catalog and be the owner of the
        parent schema, or be the owner of the table and have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.1/unity-catalog/tables/{full_name}', headers=headers)

    def exists(self, full_name: str) -> TableExistsResponse:
        """Get boolean reflecting if table exists.
        
        Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one
        of the following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the
        owner of the parent schema and have the USE_CATALOG privilege on the parent catalog * Have the
        **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema,
        and either be the table owner or have the SELECT privilege on the table. * Have BROWSE privilege on
        the parent catalog * Have BROWSE privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        
        :returns: :class:`TableExistsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/tables/{full_name}/exists', headers=headers)
        return TableExistsResponse.from_dict(res)

    def get(self, full_name: str, *, include_delta_metadata: Optional[bool] = None) -> TableInfo:
        """Get a table.
        
        Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the
        following requirements: * Be a metastore admin * Be the owner of the parent catalog * Be the owner of
        the parent schema and have the USE_CATALOG privilege on the parent catalog * Have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema, and either be
        the table owner or have the SELECT privilege on the table.
        
        :param full_name: str
          Full name of the table.
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        
        :returns: :class:`TableInfo`
        """

        query = {}
        if include_delta_metadata is not None: query['include_delta_metadata'] = include_delta_metadata
        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/tables/{full_name}', query=query, headers=headers)
        return TableInfo.from_dict(res)

    def list(self,
             catalog_name: str,
             schema_name: str,
             *,
             include_delta_metadata: Optional[bool] = None,
             max_results: Optional[int] = None,
             omit_columns: Optional[bool] = None,
             omit_properties: Optional[bool] = None,
             page_token: Optional[str] = None) -> Iterator[TableInfo]:
        """List tables.
        
        Gets an array of all tables for the current metastore under the parent catalog and schema. The caller
        must be a metastore admin or an owner of (or have the **SELECT** privilege on) the table. For the
        latter case, the caller must also be the owner or have the **USE_CATALOG** privilege on the parent
        catalog and the **USE_SCHEMA** privilege on the parent schema. There is no guarantee of a specific
        ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for tables of interest.
        :param schema_name: str
          Parent schema of tables.
        :param include_delta_metadata: bool (optional)
          Whether delta metadata should be included in the response.
        :param max_results: int (optional)
          Maximum number of tables to return. If not set, all the tables are returned (not recommended). -
          when set to a value greater than 0, the page length is the minimum of this value and a server
          configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param omit_columns: bool (optional)
          Whether to omit the columns of the table from the response or not.
        :param omit_properties: bool (optional)
          Whether to omit the properties of the table from the response or not.
        :param page_token: str (optional)
          Opaque token to send for the next page of results (pagination).
        
        :returns: Iterator over :class:`TableInfo`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if include_delta_metadata is not None: query['include_delta_metadata'] = include_delta_metadata
        if max_results is not None: query['max_results'] = max_results
        if omit_columns is not None: query['omit_columns'] = omit_columns
        if omit_properties is not None: query['omit_properties'] = omit_properties
        if page_token is not None: query['page_token'] = page_token
        if schema_name is not None: query['schema_name'] = schema_name
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/tables', query=query, headers=headers)
            if 'tables' in json:
                for v in json['tables']:
                    yield TableInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def list_summaries(self,
                       catalog_name: str,
                       *,
                       max_results: Optional[int] = None,
                       page_token: Optional[str] = None,
                       schema_name_pattern: Optional[str] = None,
                       table_name_pattern: Optional[str] = None) -> Iterator[TableSummary]:
        """List table summaries.
        
        Gets an array of summaries for tables for a schema and catalog within the metastore. The table
        summaries returned are either:
        
        * summaries for tables (within the current metastore and parent catalog and schema), when the user is
        a metastore admin, or: * summaries for tables and schemas (within the current metastore and parent
        catalog) for which the user has ownership or the **SELECT** privilege on the table and ownership or
        **USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the
        **USE_CATALOG** privilege on the parent catalog.
        
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          Name of parent catalog for tables of interest.
        :param max_results: int (optional)
          Maximum number of summaries for tables to return. If not set, the page length is set to a server
          configured value (10000, as of 1/5/2024). - when set to a value greater than 0, the page length is
          the minimum of this value and a server configured value (10000, as of 1/5/2024); - when set to 0,
          the page length is set to a server configured value (10000, as of 1/5/2024) (recommended); - when
          set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        :param schema_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.
        :param table_name_pattern: str (optional)
          A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.
        
        :returns: Iterator over :class:`TableSummary`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        if schema_name_pattern is not None: query['schema_name_pattern'] = schema_name_pattern
        if table_name_pattern is not None: query['table_name_pattern'] = table_name_pattern
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/table-summaries', query=query, headers=headers)
            if 'tables' in json:
                for v in json['tables']:
                    yield TableSummary.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def update(self, full_name: str, *, owner: Optional[str] = None):
        """Update a table owner.
        
        Change the owner of the table. The caller must be the owner of the parent catalog, have the
        **USE_CATALOG** privilege on the parent catalog and be the owner of the parent schema, or be the owner
        of the table and have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        :param full_name: str
          Full name of the table.
        :param owner: str (optional)
        
        
        """
        body = {}
        if owner is not None: body['owner'] = owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        self._api.do('PATCH', f'/api/2.1/unity-catalog/tables/{full_name}', body=body, headers=headers)


class VolumesAPI:
    """Volumes are a Unity Catalog (UC) capability for accessing, storing, governing, organizing and processing
    files. Use cases include running machine learning on unstructured data such as image, audio, video, or PDF
    files, organizing data sets during the data exploration stages in data science, working with libraries
    that require access to the local file system on cluster machines, storing library and config files of
    arbitrary formats such as .whl or .txt centrally and providing secure access across workspaces to it, or
    transforming and querying non-tabular data files in ETL."""

    def __init__(self, api_client):
        self._api = api_client

    def create(self,
               catalog_name: str,
               schema_name: str,
               name: str,
               volume_type: VolumeType,
               *,
               comment: Optional[str] = None,
               storage_location: Optional[str] = None) -> VolumeInfo:
        """Create a Volume.
        
        Creates a new volume.
        
        The user could create either an external volume or a managed volume. An external volume will be
        created in the specified external location, while a managed volume will be located in the default
        location which is specified by the parent schema, or the parent catalog, or the Metastore.
        
        For the volume creation to succeed, the user must satisfy following conditions: - The caller must be a
        metastore admin, or be the owner of the parent catalog and schema, or have the **USE_CATALOG**
        privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema. - The caller
        must have **CREATE VOLUME** privilege on the parent schema.
        
        For an external volume, following conditions also need to satisfy - The caller must have **CREATE
        EXTERNAL VOLUME** privilege on the external location. - There are no other tables, nor volumes
        existing in the specified storage location. - The specified storage location is not under the location
        of other tables, nor volumes, or catalogs or schemas.
        
        :param catalog_name: str
          The name of the catalog where the schema and the volume are
        :param schema_name: str
          The name of the schema where the volume is
        :param name: str
          The name of the volume
        :param volume_type: :class:`VolumeType`
        :param comment: str (optional)
          The comment attached to the volume
        :param storage_location: str (optional)
          The storage location on the cloud
        
        :returns: :class:`VolumeInfo`
        """
        body = {}
        if catalog_name is not None: body['catalog_name'] = catalog_name
        if comment is not None: body['comment'] = comment
        if name is not None: body['name'] = name
        if schema_name is not None: body['schema_name'] = schema_name
        if storage_location is not None: body['storage_location'] = storage_location
        if volume_type is not None: body['volume_type'] = volume_type.value
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('POST', '/api/2.1/unity-catalog/volumes', body=body, headers=headers)
        return VolumeInfo.from_dict(res)

    def delete(self, name: str):
        """Delete a Volume.
        
        Deletes a volume from the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        
        
        """

        headers = {}

        self._api.do('DELETE', f'/api/2.1/unity-catalog/volumes/{name}', headers=headers)

    def list(self,
             catalog_name: str,
             schema_name: str,
             *,
             max_results: Optional[int] = None,
             page_token: Optional[str] = None) -> Iterator[VolumeInfo]:
        """List Volumes.
        
        Gets an array of volumes for the current metastore under the parent catalog and schema.
        
        The returned volumes are filtered based on the privileges of the calling user. For example, the
        metastore admin is able to list all the volumes. A regular user needs to be the owner or have the
        **READ VOLUME** privilege on the volume to recieve the volumes in the response. For the latter case,
        the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the
        **USE_SCHEMA** privilege on the parent schema.
        
        There is no guarantee of a specific ordering of the elements in the array.
        
        :param catalog_name: str
          The identifier of the catalog
        :param schema_name: str
          The identifier of the schema
        :param max_results: int (optional)
          Maximum number of volumes to return (page length).
          
          If not set, the page length is set to a server configured value (10000, as of 1/29/2024). - when set
          to a value greater than 0, the page length is the minimum of this value and a server configured
          value (10000, as of 1/29/2024); - when set to 0, the page length is set to a server configured value
          (10000, as of 1/29/2024) (recommended); - when set to a value less than 0, an invalid parameter
          error is returned;
          
          Note: this parameter controls only the maximum number of volumes to return. The actual number of
          volumes returned in a page may be smaller than this value, including 0, even if there are more
          pages.
        :param page_token: str (optional)
          Opaque token returned by a previous request. It must be included in the request to retrieve the next
          page of results (pagination).
        
        :returns: Iterator over :class:`VolumeInfo`
        """

        query = {}
        if catalog_name is not None: query['catalog_name'] = catalog_name
        if max_results is not None: query['max_results'] = max_results
        if page_token is not None: query['page_token'] = page_token
        if schema_name is not None: query['schema_name'] = schema_name
        headers = {'Accept': 'application/json', }

        while True:
            json = self._api.do('GET', '/api/2.1/unity-catalog/volumes', query=query, headers=headers)
            if 'volumes' in json:
                for v in json['volumes']:
                    yield VolumeInfo.from_dict(v)
            if 'next_page_token' not in json or not json['next_page_token']:
                return
            query['page_token'] = json['next_page_token']

    def read(self, name: str) -> VolumeInfo:
        """Get a Volume.
        
        Gets a volume from the metastore for a specific catalog and schema.
        
        The caller must be a metastore admin or an owner of (or have the **READ VOLUME** privilege on) the
        volume. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege
        on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        
        :returns: :class:`VolumeInfo`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.1/unity-catalog/volumes/{name}', headers=headers)
        return VolumeInfo.from_dict(res)

    def update(self,
               name: str,
               *,
               comment: Optional[str] = None,
               new_name: Optional[str] = None,
               owner: Optional[str] = None) -> VolumeInfo:
        """Update a Volume.
        
        Updates the specified volume under the specified parent catalog and schema.
        
        The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must
        also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**
        privilege on the parent schema.
        
        Currently only the name, the owner or the comment of the volume could be updated.
        
        :param name: str
          The three-level (fully qualified) name of the volume
        :param comment: str (optional)
          The comment attached to the volume
        :param new_name: str (optional)
          New name for the volume.
        :param owner: str (optional)
          The identifier of the user who owns the volume
        
        :returns: :class:`VolumeInfo`
        """
        body = {}
        if comment is not None: body['comment'] = comment
        if new_name is not None: body['new_name'] = new_name
        if owner is not None: body['owner'] = owner
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.1/unity-catalog/volumes/{name}', body=body, headers=headers)
        return VolumeInfo.from_dict(res)


class WorkspaceBindingsAPI:
    """A securable in Databricks can be configured as __OPEN__ or __ISOLATED__. An __OPEN__ securable can be
    accessed from any workspace, while an __ISOLATED__ securable can only be accessed from a configured list
    of workspaces. This API allows you to configure (bind) securables to workspaces.
    
    NOTE: The __isolation_mode__ is configured for the securable itself (using its Update method) and the
    workspace bindings are only consulted when the securable's __isolation_mode__ is set to __ISOLATED__.
    
    A securable's workspace bindings can be configured by a metastore admin or the owner of the securable.
    
    The original path (/api/2.1/unity-catalog/workspace-bindings/catalogs/{name}) is deprecated. Please use
    the new path (/api/2.1/unity-catalog/bindings/{securable_type}/{securable_name}) which introduces the
    ability to bind a securable in READ_ONLY mode (catalogs only).
    
    Securables that support binding: - catalog"""

    def __init__(self, api_client):
        self._api = api_client

    def get(self, name: str) -> CurrentWorkspaceBindings:
        """Get catalog workspace bindings.
        
        Gets workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.
        
        :param name: str
          The name of the catalog.
        
        :returns: :class:`CurrentWorkspaceBindings`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/workspace-bindings/catalogs/{name}',
                           headers=headers)
        return CurrentWorkspaceBindings.from_dict(res)

    def get_bindings(self, securable_type: str, securable_name: str) -> WorkspaceBindingsResponse:
        """Get securable workspace bindings.
        
        Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the
        securable.
        
        :param securable_type: str
          The type of the securable.
        :param securable_name: str
          The name of the securable.
        
        :returns: :class:`WorkspaceBindingsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.1/unity-catalog/bindings/{securable_type}/{securable_name}',
                           headers=headers)
        return WorkspaceBindingsResponse.from_dict(res)

    def update(self,
               name: str,
               *,
               assign_workspaces: Optional[List[int]] = None,
               unassign_workspaces: Optional[List[int]] = None) -> CurrentWorkspaceBindings:
        """Update catalog workspace bindings.
        
        Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the
        catalog.
        
        :param name: str
          The name of the catalog.
        :param assign_workspaces: List[int] (optional)
          A list of workspace IDs.
        :param unassign_workspaces: List[int] (optional)
          A list of workspace IDs.
        
        :returns: :class:`CurrentWorkspaceBindings`
        """
        body = {}
        if assign_workspaces is not None: body['assign_workspaces'] = [v for v in assign_workspaces]
        if unassign_workspaces is not None: body['unassign_workspaces'] = [v for v in unassign_workspaces]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/workspace-bindings/catalogs/{name}',
                           body=body,
                           headers=headers)
        return CurrentWorkspaceBindings.from_dict(res)

    def update_bindings(self,
                        securable_type: str,
                        securable_name: str,
                        *,
                        add: Optional[List[WorkspaceBinding]] = None,
                        remove: Optional[List[WorkspaceBinding]] = None) -> WorkspaceBindingsResponse:
        """Update securable workspace bindings.
        
        Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the
        securable.
        
        :param securable_type: str
          The type of the securable.
        :param securable_name: str
          The name of the securable.
        :param add: List[:class:`WorkspaceBinding`] (optional)
          List of workspace bindings
        :param remove: List[:class:`WorkspaceBinding`] (optional)
          List of workspace bindings
        
        :returns: :class:`WorkspaceBindingsResponse`
        """
        body = {}
        if add is not None: body['add'] = [v.as_dict() for v in add]
        if remove is not None: body['remove'] = [v.as_dict() for v in remove]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.1/unity-catalog/bindings/{securable_type}/{securable_name}',
                           body=body,
                           headers=headers)
        return WorkspaceBindingsResponse.from_dict(res)
