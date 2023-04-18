import type { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  /** Date (isoformat) */
  Date: any;
  /** Date with time (isoformat) */
  DateTime: any;
  UUID: any;
};

export type AdminUser = {
  __typename?: 'AdminUser';
  createdAt: Scalars['DateTime'];
  email: Scalars['String'];
  firstName: Scalars['String'];
  id: Scalars['UUID'];
  isActive: Scalars['Boolean'];
  lastName: Scalars['String'];
  lastSeen: Scalars['DateTime'];
};

export enum DirectionEnum {
  Asc = 'ASC',
  Desc = 'DESC'
}

/** A toxicity label */
export enum Label {
  IdentityHate = 'IDENTITY_HATE',
  Insult = 'INSULT',
  Obscene = 'OBSCENE',
  Threat = 'THREAT',
  Toxic = 'TOXIC'
}

export type LabelType = {
  __typename?: 'LabelType';
  label: Label;
  score: Scalars['Float'];
  severity: Severity;
};

/** A user's social media account */
export type LinkedAccount = {
  __typename?: 'LinkedAccount';
  logoUrl: Scalars['String'];
  platform: Platform;
};

export type Mutation = {
  __typename?: 'Mutation';
  /** Accept a label for a message */
  acceptLabel: Scalars['Boolean'];
  deleteAdmin: Scalars['Boolean'];
  deleteUser: Scalars['Boolean'];
  deleteUsers: Scalars['Boolean'];
  disableAdmin: Scalars['Boolean'];
  disableUser: Scalars['Boolean'];
  disableUsers: Scalars['Boolean'];
  /** Refuse a label for a message */
  refuseLabel: Scalars['Boolean'];
  /** Skip a label, e.g. because you're not sure */
  skipLabel: Scalars['Boolean'];
  updateAdmin: Scalars['Boolean'];
  updateUser: Scalars['Boolean'];
};


export type MutationAcceptLabelArgs = {
  messageId: Scalars['ID'];
};


export type MutationDeleteAdminArgs = {
  adminId: Scalars['ID'];
};


export type MutationDeleteUserArgs = {
  userId: Scalars['ID'];
};


export type MutationDeleteUsersArgs = {
  userIds: Array<Scalars['ID']>;
};


export type MutationDisableAdminArgs = {
  adminId: Scalars['ID'];
};


export type MutationDisableUserArgs = {
  userId: Scalars['ID'];
};


export type MutationDisableUsersArgs = {
  userIds: Array<Scalars['ID']>;
};


export type MutationRefuseLabelArgs = {
  messageId: Scalars['ID'];
};


export type MutationSkipLabelArgs = {
  messageId: Scalars['ID'];
};


export type MutationUpdateAdminArgs = {
  adminId: Scalars['ID'];
  input: UpdateUserInput;
};


export type MutationUpdateUserArgs = {
  input: UpdateUserInput;
  userId: Scalars['ID'];
};

/** Subscription plan */
export enum Plan {
  Basic = 'BASIC',
  Safe = 'SAFE'
}

/** Social media platform */
export enum Platform {
  Facebook = 'FACEBOOK',
  Instagram = 'INSTAGRAM',
  Twitter = 'TWITTER'
}

export type Query = {
  __typename?: 'Query';
  admins: Array<AdminUser>;
  labelingHistory: Array<VerifiedLabel>;
  labelingTasks: Array<UnverifiedLabel>;
  users: Array<User>;
};


export type QueryUsersArgs = {
  filters?: InputMaybe<UserFiltersInput>;
  orderBy?: InputMaybe<UserOrderByInput>;
};

/** Severity of a toxicity label */
export enum Severity {
  High = 'HIGH',
  Low = 'LOW',
  Medium = 'MEDIUM'
}

/** Statistics for a given timeframe */
export type StatisticsType = {
  __typename?: 'StatisticsType';
  blockedMessages: Scalars['Int'];
  totalMessages: Scalars['Int'];
  toxicMessages: Scalars['Int'];
};

export type UnverifiedLabel = {
  __typename?: 'UnverifiedLabel';
  id: Scalars['ID'];
  label: LabelType;
  message: Scalars['String'];
};

export type UpdateUserInput = {
  email?: InputMaybe<Scalars['String']>;
  firstName?: InputMaybe<Scalars['String']>;
  lastName?: InputMaybe<Scalars['String']>;
};

/** A user account */
export type User = {
  __typename?: 'User';
  age: Scalars['Int'];
  avatarUrl: Scalars['String'];
  birthday: Scalars['Date'];
  createdAt: Scalars['DateTime'];
  email: Scalars['String'];
  firstName: Scalars['String'];
  fullName: Scalars['String'];
  id: Scalars['UUID'];
  identityVerified: Scalars['Boolean'];
  isMinor: Scalars['Boolean'];
  isParent: Scalars['Boolean'];
  lastName: Scalars['String'];
  linkedAccounts: Array<LinkedAccount>;
  onboardingCompleted: Scalars['Boolean'];
  plan: Plan;
  stats: UserStatisticsType;
};

/** User field names */
export enum UserField {
  Age = 'age',
  AvatarUrl = 'avatarUrl',
  Birthday = 'birthday',
  CreatedAt = 'createdAt',
  Email = 'email',
  FirstName = 'firstName',
  FullName = 'fullName',
  Id = 'id',
  IdentityDocumentType = 'identityDocumentType',
  IdentityDocumentUrl = 'identityDocumentUrl',
  IdentityVerified = 'identityVerified',
  IsActive = 'isActive',
  IsMinor = 'isMinor',
  IsParent = 'isParent',
  LastName = 'lastName',
  LastSeen = 'lastSeen',
  LinkedAccounts = 'linkedAccounts',
  OnboardingCompleted = 'onboardingCompleted',
  Password = 'password',
  Plan = 'plan',
  UpdatedAt = 'updatedAt'
}

export type UserFiltersInput = {
  plan?: InputMaybe<Plan>;
  query?: InputMaybe<Scalars['String']>;
};

export type UserOrderByInput = {
  direction?: DirectionEnum;
  field: UserField;
};

/** User statistics */
export type UserStatisticsType = {
  __typename?: 'UserStatisticsType';
  day: StatisticsType;
  month: StatisticsType;
  quarter: StatisticsType;
  twoMonths: StatisticsType;
  week: StatisticsType;
};

export type VerifiedLabel = {
  __typename?: 'VerifiedLabel';
  id: Scalars['ID'];
  label: LabelType;
  message: Scalars['String'];
  verifiedAt: Scalars['DateTime'];
  verifiedBy: Scalars['String'];
};

export type GetUsersQueryVariables = Exact<{
  filters?: InputMaybe<UserFiltersInput>;
  orderBy?: InputMaybe<UserOrderByInput>;
}>;


export type GetUsersQuery = { __typename?: 'Query', users: Array<{ __typename?: 'User', id: any, email: string, firstName: string, lastName: string, createdAt: any, fullName: string, avatarUrl: string, birthday: any, onboardingCompleted: boolean, identityVerified: boolean, age: number, isMinor: boolean, isParent: boolean, plan: Plan, linkedAccounts: Array<{ __typename?: 'LinkedAccount', platform: Platform, logoUrl: string }>, stats: { __typename?: 'UserStatisticsType', day: { __typename?: 'StatisticsType', totalMessages: number, toxicMessages: number, blockedMessages: number }, week: { __typename?: 'StatisticsType', totalMessages: number, toxicMessages: number, blockedMessages: number }, month: { __typename?: 'StatisticsType', totalMessages: number, toxicMessages: number, blockedMessages: number }, twoMonths: { __typename?: 'StatisticsType', totalMessages: number, toxicMessages: number, blockedMessages: number }, quarter: { __typename?: 'StatisticsType', totalMessages: number, toxicMessages: number, blockedMessages: number } } }> };


export const GetUsersDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetUsers"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"filters"}},"type":{"kind":"NamedType","name":{"kind":"Name","value":"UserFiltersInput"}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"orderBy"}},"type":{"kind":"NamedType","name":{"kind":"Name","value":"UserOrderByInput"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"users"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"filters"},"value":{"kind":"Variable","name":{"kind":"Name","value":"filters"}}},{"kind":"Argument","name":{"kind":"Name","value":"orderBy"},"value":{"kind":"Variable","name":{"kind":"Name","value":"orderBy"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"email"}},{"kind":"Field","name":{"kind":"Name","value":"firstName"}},{"kind":"Field","name":{"kind":"Name","value":"lastName"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}},{"kind":"Field","name":{"kind":"Name","value":"fullName"}},{"kind":"Field","name":{"kind":"Name","value":"avatarUrl"}},{"kind":"Field","name":{"kind":"Name","value":"birthday"}},{"kind":"Field","name":{"kind":"Name","value":"onboardingCompleted"}},{"kind":"Field","name":{"kind":"Name","value":"identityVerified"}},{"kind":"Field","name":{"kind":"Name","value":"age"}},{"kind":"Field","name":{"kind":"Name","value":"isMinor"}},{"kind":"Field","name":{"kind":"Name","value":"isParent"}},{"kind":"Field","name":{"kind":"Name","value":"plan"}},{"kind":"Field","name":{"kind":"Name","value":"linkedAccounts"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"platform"}},{"kind":"Field","name":{"kind":"Name","value":"logoUrl"}}]}},{"kind":"Field","name":{"kind":"Name","value":"stats"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"day"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"totalMessages"}},{"kind":"Field","name":{"kind":"Name","value":"toxicMessages"}},{"kind":"Field","name":{"kind":"Name","value":"blockedMessages"}}]}},{"kind":"Field","name":{"kind":"Name","value":"week"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"totalMessages"}},{"kind":"Field","name":{"kind":"Name","value":"toxicMessages"}},{"kind":"Field","name":{"kind":"Name","value":"blockedMessages"}}]}},{"kind":"Field","name":{"kind":"Name","value":"month"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"totalMessages"}},{"kind":"Field","name":{"kind":"Name","value":"toxicMessages"}},{"kind":"Field","name":{"kind":"Name","value":"blockedMessages"}}]}},{"kind":"Field","name":{"kind":"Name","value":"twoMonths"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"totalMessages"}},{"kind":"Field","name":{"kind":"Name","value":"toxicMessages"}},{"kind":"Field","name":{"kind":"Name","value":"blockedMessages"}}]}},{"kind":"Field","name":{"kind":"Name","value":"quarter"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"totalMessages"}},{"kind":"Field","name":{"kind":"Name","value":"toxicMessages"}},{"kind":"Field","name":{"kind":"Name","value":"blockedMessages"}}]}}]}}]}}]}}]} as unknown as DocumentNode<GetUsersQuery, GetUsersQueryVariables>;