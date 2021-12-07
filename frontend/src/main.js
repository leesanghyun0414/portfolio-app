// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import { createApp, provide, h } from "vue";
import { DefaultApolloClient } from "@vue/apollo-composable";
import App from "./App.vue";
import { apolloClient } from "./api/graphql/client";
import "./index.css";
import { router } from "./router/router";
const app = createApp({
    setup() {
        provide(DefaultApolloClient, apolloClient);
    },
    render: () => h(App),
});
app.use(router);
app.mount("#counter");
//# sourceMappingURL=main.js.map