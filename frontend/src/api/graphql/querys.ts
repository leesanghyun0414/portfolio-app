import gql from "graphql-tag"
import { DocumentNode } from "graphql"

export const ALL_POSTS: DocumentNode = gql`
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
`
export const POST_BY_AUTHOR = gql`
  query ($username: String) {
    postByAuthor(username: $username) {
      id
      author {
        user {
          username
        }
      }
      title
      subtitle
    }
  }
`
export const POST_DETAIL = gql`
  query postDetail($postId: ID!) {
    postById(postId: $postId) {
      title
      subtitle
    }
    postBody(postId: $postId) {
      text
    }
    totalLikeCountByPost(postId: $postId)
  }
`
