<template>
  <div>
    <div>
      <!-- <Logo /> -->
      <h1 style="text-align: center; padding:10px">イベント横断サーチ</h1>
      <basic-multi-form :items="fields" @decide="apiPostTrigger">
      </basic-multi-form>
      <!-- <h1 class="title">
        event_front
      </h1> -->
    </div>
    <div>
      <card :items="response"></card>
    </div>
    <div class="links">
      <a
        href="https://nuxtjs.org/"
        target="_blank"
        rel="noopener noreferrer"
        class="button--green"
      >
        Documentation
      </a>
      <a
        href="https://github.com/nuxt/nuxt.js"
        target="_blank"
        rel="noopener noreferrer"
        class="button--grey"
      >
        GitHub
      </a>
    </div>
  </div>
</template>

<script lang="ts">
// import Vue from 'vue'
import { defineComponent } from '@nuxtjs/composition-api'
import BasicMultiForm from '@/components/searchForm.vue'
import card from '@/components/eventTable.vue'
import useSampleApi from '~/composition/useSampleApi'

type iField = {
  label: string
  key: string
  type: string
  min?: number
  max?: number
}
export default defineComponent({
  components: { BasicMultiForm, card },

  setup(_props, { root }) {
    const fields: iField[] = [
      { label: 'キーワード', key: 'keyword', type: 'text' },
      { label: '開催地', key: 'address', type: 'text' },
      { label: 'From', key: 'start_from', type: 'date' },
      { label: 'To', key: 'start_to', type: 'date' },
      { label: '取得イベント数', key: 'limit', type: 'number', min: 0 }
      // { label: '並び順', key: 'aiu', type: 'number', min: 0, max: 1 }
    ]
    const { $axios } = root
    const { response, isLoading, apiPostTrigger } = useSampleApi($axios)
    return {
      isLoading,
      response,
      apiPostTrigger,
      fields
    }
  }
})
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
