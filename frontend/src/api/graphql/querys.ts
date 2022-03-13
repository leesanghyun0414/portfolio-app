import gql from "graphql-tag"
import { DocumentNode } from "graphql"

export const GET_ALLCATEGORY: DocumentNode = gql`
  {
    allCategory
  }
`

export const GET_MENU_BY_CATEGORY_ID: DocumentNode = gql`
  query getMenuByCategoryId($categoryId: String!) {
    menuByCategoryId(categoryId: $categoryId)
  }
`
