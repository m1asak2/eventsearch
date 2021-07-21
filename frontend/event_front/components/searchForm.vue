<template>
  <div class="container">
    <form action="">
      <div class="form-group">
        <label for="keyword">キーワード</label>
        <input
          v-model="state.displayitem.keyword"
          required
          type="text"
          placeholder="AND検索"
          style="width :100%"
        />
      </div>
      <div class="form-group">
        <label class="d-block">期間</label>
        <div class="form-check-inline" style="width:100%">
          <input
            id="id_start_from"
            v-model="state.displayitem.start_from"
            type="date"
            name="start_from"
            class="form-control"
          />
          <span style="min-width :40px">から</span>
          <label for="period"></label>
          <select
            id="period"
            v-model="state.displayitem.period"
            name="period"
            class="form-control"
          >
            <option value="0">当日</option>
            <option value="10">10日先まで</option>
            <option value="20">20日先まで</option>
            <option value="30">30日先まで</option>
            <option value="60">60日先まで</option>
            <option value="90">90日先まで</option>
          </select>
          <!-- <span style="min-width :50px"></span> -->
        </div>
      </div>

      <div class="form-check-inline" style="width:100%">
        <div class="form-group" style="width:50%">
          <label for="">開催地</label>
          <input
            v-model="state.displayitem.address"
            type="text"
            style="width:95%"
            placeholder="OR検索"
          />
        </div>
        <div class="form-group" style="width:50%">
          <label for="limit">取得イベント数</label>
          <select
            id="limit"
            v-model="state.displayitem.limit"
            name="limit"
            class="form-control"
          >
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <span v-for="(target, index) in state.displayitem.target" :key="index">
          <input
            :id="target"
            v-model="state.targets"
            type="checkbox"
            :value="target"
          />
          <label :for="target" style="margin-right:15px">{{ target }} </label>
        </span>
      </div>
      <div class="flex-container">
        <button
          type="submit"
          class="btn btn-primary"
          style=" width:70%"
          @click="onSubmit"
        >
          Search
        </button>
        <button
          type="submit"
          class="btn btn-warning"
          style=" width:25%"
          @click="onSave"
        >
          Save
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import {
  defineComponent,
  // computed,
  reactive,
  PropType,
  watch
  // watchEffect
} from '@nuxtjs/composition-api'
import { DisplayForm } from '@/types/interfaces'
import { getDate } from '@/composition/GetDate'
interface stateBase {
  targets: string[]
  displayitem: DisplayForm
}
export default defineComponent({
  props: {
    items: {
      type: Object as PropType<DisplayForm>,
      default: () => undefined
    }
  },
  setup(props, { emit }) {
    const state = reactive<stateBase>({
      targets: [],
      displayitem: {
        keyword: '',
        address: '',
        limit: 10,
        start_from: '',
        period: '',
        // target: ['connpass', 'doorkeeper', 'techplay']
        target: ['connpass', 'doorkeeper']
      }
    })
    state.displayitem.start_from = getDate()
    state.displayitem.period = '30'
    const Clear = () => {
      state.displayitem.keyword = ''
      state.displayitem.address = ''
      state.displayitem.start_from = getDate()
      state.displayitem.period = '30'
      state.targets = []
    }
    const onSubmit = (evt: Event) => {
      evt.preventDefault()
      emit('search', GetSearchData())
    }
    const onSave = (evt: Event) => {
      evt.preventDefault()

      emit('save', GetSearchData())
      // Clear()
    }
    const GetSearchData = () => {
      const send = Object.assign({}, state.displayitem)
      send.target = state.targets
      return send
    }
    const localprop: DisplayForm = {
      keyword: props.items.keyword,
      address: props.items.address,
      period: props.items.period,
      start_from: props.items.start_from,
      target: props.items.target,
      limit: props.items.limit
    }
    watch(props, () => {
      state.displayitem.keyword = props.items.keyword
      state.displayitem.address = props.items.address
      state.displayitem.start_from = props.items.start_from
      state.displayitem.period = props.items.period
      state.targets = props.items.target
      state.displayitem.limit = props.items.limit
    })
    return {
      state,
      GetSearchData,
      localprop,
      onSubmit,
      onSave,
      getDate,
      Clear
    }
  }
})
</script>
<style scoped>
label {
  font-weight: bold;
}
.form-group {
  text-align: left;
}
.wrapper {
  /* width: 80%; */
  grid-template-rows: 50px 200px;
  grid-template-columns: 1fr 2fr;
}
.flex-container {
  display: flex;
  justify-content: space-between;
}
.container {
  max-width: 600px;

  width: 80%;
}
.form-group {
  width: 100%;
  min-width: 150px;
}
</style>
