import gql from 'graphql-tag';
import * as VueApolloComposable from 'vue';
import * as VueCompositionApi from '@vue/composition-api';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type ReactiveFunction<TParam> = () => TParam;
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  GenericScalar: any;
};

export type CategoryType = {
  __typename?: 'CategoryType';
  id: Scalars['ID'];
  name: Scalars['String'];
  numchild: Scalars['Int'];
  path: Scalars['String'];
};

export type MenuType = {
  __typename?: 'MenuType';
  calorie: Scalars['Int'];
  category: CategoryType;
  image: Scalars['String'];
  name: Scalars['String'];
  price: Scalars['Int'];
};

export type Query = {
  __typename?: 'Query';
  allCategory?: Maybe<Scalars['GenericScalar']>;
  allMenu?: Maybe<Array<Maybe<MenuType>>>;
  menuByCategoryId?: Maybe<Array<Maybe<MenuType>>>;
  menuById?: Maybe<MenuType>;
  menuPath?: Maybe<MenuType>;
};


export type QueryMenuByCategoryIdArgs = {
  categoryId: Scalars['ID'];
};


export type QueryMenuByIdArgs = {
  isReleased?: InputMaybe<Scalars['Boolean']>;
  menuId: Scalars['ID'];
};


export type QueryMenuPathArgs = {
  menuId: Scalars['ID'];
};


export const Document = gql`
    {
  allCategory
}
    `;
export const GetMenuByCategoryIdDocument = gql`
    query getMenuByCategoryId($categoryId: ID!) {
  menuByCategoryId(categoryId: $categoryId) {
    name
  }
}
    `;

/**
 * __useGetMenuByCategoryIdQuery__
 *
 * To run a query within a Vue component, call `useGetMenuByCategoryIdQuery` and pass it any options that fit your needs.
 * When your component renders, `useGetMenuByCategoryIdQuery` returns an object from Apollo Client that contains result, loading and error properties
 * you can use to render your UI.
 *
 * @param variables that will be passed into the query
 * @param options that will be passed into the query, supported options are listed on: https://v4.apollo.vuejs.org/guide-composable/query.html#options;
 *
 * @example
 * const { result, loading, error } = useGetMenuByCategoryIdQuery({
 *   categoryId: // value for 'categoryId'
 * });
 */
export function useGetMenuByCategoryIdQuery(variables: GetMenuByCategoryIdQueryVariables | VueCompositionApi.Ref<GetMenuByCategoryIdQueryVariables> | ReactiveFunction<GetMenuByCategoryIdQueryVariables>, options: VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables> | VueCompositionApi.Ref<VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>> | ReactiveFunction<VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>> = {}) {
  return VueApolloComposable.useQuery<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>(GetMenuByCategoryIdDocument, variables, options);
}
export function useGetMenuByCategoryIdLazyQuery(variables: GetMenuByCategoryIdQueryVariables | VueCompositionApi.Ref<GetMenuByCategoryIdQueryVariables> | ReactiveFunction<GetMenuByCategoryIdQueryVariables>, options: VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables> | VueCompositionApi.Ref<VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>> | ReactiveFunction<VueApolloComposable.UseQueryOptions<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>> = {}) {
  return VueApolloComposable.useLazyQuery<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>(GetMenuByCategoryIdDocument, variables, options);
}
export type GetMenuByCategoryIdQueryCompositionFunctionResult = VueApolloComposable.UseQueryReturn<GetMenuByCategoryIdQuery, GetMenuByCategoryIdQueryVariables>;
export const GetMenuByIdDocument = gql`
    query getMenuById($menuId: ID!, $isReleased: Boolean) {
  menuById(menuId: $menuId, isReleased: $isReleased) {
    name
    calorie
    price
    image
  }
}
    `;

/**
 * __useGetMenuByIdQuery__
 *
 * To run a query within a Vue component, call `useGetMenuByIdQuery` and pass it any options that fit your needs.
 * When your component renders, `useGetMenuByIdQuery` returns an object from Apollo Client that contains result, loading and error properties
 * you can use to render your UI.
 *
 * @param variables that will be passed into the query
 * @param options that will be passed into the query, supported options are listed on: https://v4.apollo.vuejs.org/guide-composable/query.html#options;
 *
 * @example
 * const { result, loading, error } = useGetMenuByIdQuery({
 *   menuId: // value for 'menuId'
 *   isReleased: // value for 'isReleased'
 * });
 */
export function useGetMenuByIdQuery(variables: GetMenuByIdQueryVariables | VueCompositionApi.Ref<GetMenuByIdQueryVariables> | ReactiveFunction<GetMenuByIdQueryVariables>, options: VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables> | VueCompositionApi.Ref<VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables>> | ReactiveFunction<VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables>> = {}) {
  return VueApolloComposable.useQuery<GetMenuByIdQuery, GetMenuByIdQueryVariables>(GetMenuByIdDocument, variables, options);
}
export function useGetMenuByIdLazyQuery(variables: GetMenuByIdQueryVariables | VueCompositionApi.Ref<GetMenuByIdQueryVariables> | ReactiveFunction<GetMenuByIdQueryVariables>, options: VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables> | VueCompositionApi.Ref<VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables>> | ReactiveFunction<VueApolloComposable.UseQueryOptions<GetMenuByIdQuery, GetMenuByIdQueryVariables>> = {}) {
  return VueApolloComposable.useLazyQuery<GetMenuByIdQuery, GetMenuByIdQueryVariables>(GetMenuByIdDocument, variables, options);
}
export type GetMenuByIdQueryCompositionFunctionResult = VueApolloComposable.UseQueryReturn<GetMenuByIdQuery, GetMenuByIdQueryVariables>;
export type Unnamed_1_QueryVariables = Exact<{ [key: string]: never; }>;


export type Unnamed_1_Query = { __typename?: 'Query', allCategory?: any | null };

export type GetMenuByCategoryIdQueryVariables = Exact<{
  categoryId: Scalars['ID'];
}>;


export type GetMenuByCategoryIdQuery = { __typename?: 'Query', menuByCategoryId?: Array<{ __typename?: 'MenuType', name: string } | null> | null };

export type GetMenuByIdQueryVariables = Exact<{
  menuId: Scalars['ID'];
  isReleased?: InputMaybe<Scalars['Boolean']>;
}>;


export type GetMenuByIdQuery = { __typename?: 'Query', menuById?: { __typename?: 'MenuType', name: string, calorie: number, price: number, image: string } | null };
