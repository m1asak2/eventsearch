module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'plugin:nuxt/recommended',
    'eslint-config-prettier' // Prettierでカバーできるルールを無効化?
  ],
  plugins: [],
  // add your custom rules here
  rules: {
    // 関数とカッコはあけない(function hoge() {/** */})
    'func-call-spacing': [2, 'never'],
    // セミコロンは禁止
    semi: [2, 'never']
  }
}
