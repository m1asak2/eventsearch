<template>
  <div>
    <Nuxt />
  </div>
</template>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

.SimpleTable {
  border-collapse: collapse;
  border-spacing: 0;
  width: 95%;
  margin: 10px;
}

.SimpleTable tr {
  border-bottom: solid 1px rgb(211, 209, 209);
  /* max-width: 50px; */
}

.SimpleTable th,
.SimpleTable td {
  text-align: left;
  font-weight: normal;
  padding: 3px;
  max-width: 400px;
  /* max-height: 10px; */
}
/*td下階層にあるimg */
.SimpleTable td > img {
  width: 5rem;
}
.SimpleTable a {
  color: black;
  border-bottom: 1px solid black;
}
</style>
