<template>
  <div>
    <div>
      <!-- <Logo /> -->
      <h1>イベント横断サーチ</h1>
      <h2>保存済み検索条件</h2>
      <div style="display:flex">
        <event-card
          v-for="(item, index) in state.savedItem"
          :key="index"
          :items="item"
          style="margin:1em 0 1em 1em"
          @set="setCondition(index)"
          @delete="deleteCondition(index)"
        ></event-card>
      </div>
      <search-form
        :items="state.displayItem"
        @search="search"
        @save="SaveCondition"
      >
      </search-form>
      <!-- <h1 class="title">
        event_front
      </h1> -->
    </div>
    <div>
      <card :items="response"></card>
    </div>
  </div>
</template>

<script lang="ts">
// import Vue from 'vue'
import {
  defineComponent,
  // computed,
  reactive,
  onMounted,
  onBeforeMount
} from '@nuxtjs/composition-api'
import SearchForm from '@/components/searchForm.vue'
import { DisplayForm, SaveForm } from '@/types/interfaces'
import card from '@/components/eventTable.vue'
import EventCard from '@/components/EventCard.vue'
// import useSampleApi from '~/composition/useSampleApi'
import useEventApi from '~/composition/useEventApi'
import { DisplayToSaveForm, SaveToDisplayForm } from '~/composition/ConvertForm'
import local from '~/store/local'
import { DisplayToSendForm } from '~/composition/ConvertDisplayForm'
class EventItems {
  savedItem: SaveForm[] = []
  displayItem: DisplayForm = {
    keyword: '',
    address: '',
    limit: 0,
    start_from: '',
    period: '',
    target: []
  }
}
export default defineComponent({
  components: { SearchForm, card, EventCard },

  setup(_props) {
    // const { $axios } = root
    // const { response, isLoading, apiPostTrigger } = useSampleApi($axios)
    const { response, isLoading, apiPostTrigger } = useEventApi()
    const { load, save, remove } = local()
    const state = reactive(new EventItems())
    const LoadItems = () => {
      // state.savedItem.push({
      //   keyword: 'javascript java',
      //   address: 'online',
      //   limit: 10,
      //   period: '30',
      //   target: ['connpass', 'doorkeeper']
      // })
      // state.savedItem.push({
      //   keyword: 'flutter dart',
      //   address: 'osaka',
      //   limit: 50,
      //   period: '10',
      //   target: ['connpass']
      // })
      // state.savedItem.push({
      //   keyword: 'vue.js nuxt',
      //   address: 'tokyo',
      //   limit: 20,
      //   period: '20',
      //   target: ['doorkeeper']
      // })
      state.savedItem = load()
    }
    const setCondition = (i: number) => {
      state.displayItem = SaveToDisplayForm(state.savedItem[i])
    }
    const deleteCondition = (i: number) => {
      // state.savedItem.splice(i, 1)
      state.savedItem = remove(i)
    }
    const created = onBeforeMount(() => {
      LoadItems()
    })
    const SaveCondition = (evt: DisplayForm) => {
      const saveItem = DisplayToSaveForm(evt)
      state.savedItem = save(saveItem)
      // load()
      // state.savedItem.push(Object.assign({}, saveItem))
    }
    const search = (data: DisplayForm) => {
      response.value = []
      apiPostTrigger(data)
    }
    return {
      state,
      search,
      onMounted,
      isLoading,
      response,
      apiPostTrigger,
      LoadItems,
      setCondition,
      created,
      SaveCondition,
      deleteCondition
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
