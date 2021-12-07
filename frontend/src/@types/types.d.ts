import gql from 'graphql-tag';
export type Maybe<T> = T | null;
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
  /**
   * The `DateTime` scalar type represents a DateTime
   * value as specified by
   * [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
   */
  DateTime: any;
};

export type AuthorType = {
  __typename?: 'AuthorType';
  bio: Scalars['String'];
  id: Scalars['ID'];
  postSet: Array<PostType>;
  user: UserType;
  website: Scalars['String'];
};

export type PostType = {
  __typename?: 'PostType';
  author: AuthorType;
  dateCreated: Scalars['DateTime'];
  dateModified: Scalars['DateTime'];
  id: Scalars['ID'];
  like: Scalars['Int'];
  publishDate?: Maybe<Scalars['DateTime']>;
  published: Scalars['Boolean'];
  subtitle: Scalars['String'];
  tag: Array<TagType>;
  text: Scalars['String'];
  title: Scalars['String'];
};

export type Query = {
  __typename?: 'Query';
  allPosts?: Maybe<Array<Maybe<PostType>>>;
  allTags?: Maybe<Array<Maybe<TagType>>>;
  authorByUser?: Maybe<AuthorType>;
  postByAuthor?: Maybe<Array<Maybe<PostType>>>;
  postByTag?: Maybe<Array<Maybe<PostType>>>;
};


export type QueryAuthorByUserArgs = {
  username?: Maybe<Scalars['String']>;
};


export type QueryPostByAuthorArgs = {
  username?: Maybe<Scalars['String']>;
};


export type QueryPostByTagArgs = {
  tag?: Maybe<Scalars['String']>;
};

export type TagType = {
  __typename?: 'TagType';
  id: Scalars['ID'];
  name: Scalars['String'];
  postSet: Array<PostType>;
};

export type UserType = {
  __typename?: 'UserType';
  dateJoined: Scalars['DateTime'];
  email: Scalars['String'];
  firstName: Scalars['String'];
  id: Scalars['ID'];
  /** ユーザーがアクティブかどうかを示します。アカウントを削除する代わりに選択を解除してください。 */
  isActive: Scalars['Boolean'];
  /** ユーザーが管理サイトにログイン可能かどうかを示します。 */
  isStaff: Scalars['Boolean'];
  /** 全ての権限を持っているとみなされます。 */
  isSuperuser: Scalars['Boolean'];
  lastLogin?: Maybe<Scalars['DateTime']>;
  lastName: Scalars['String'];
  password: Scalars['String'];
  profile?: Maybe<AuthorType>;
  /** この項目は必須です。半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。 */
  username: Scalars['String'];
};


export const Document = gql`
    {
  allPosts {
    id
    author {
      user {
        id
        username
        lastLogin
      }
      bio
    }
  }
}
    `;
export type Unnamed_1_QueryVariables = Exact<{ [key: string]: never; }>;


export type Unnamed_1_Query = { __typename?: 'Query', allPosts?: Maybe<Array<Maybe<{ __typename?: 'PostType', id: string, author: { __typename?: 'AuthorType', bio: string, user: { __typename?: 'UserType', id: string, username: string, lastLogin?: Maybe<any> } } }>>> };
