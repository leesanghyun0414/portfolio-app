import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core"
import { API_SERVER } from "../../config/api_roots"

// HTTP connection to the API
const httpLink = createHttpLink({
  // You should use an absolute URL here
  uri: API_SERVER,
})

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
export const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})
