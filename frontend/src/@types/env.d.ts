interface ImportMetaEnv {
  readonly VITE_API_SERVER: string
  readonly VITE_ASSET_ROOT: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
