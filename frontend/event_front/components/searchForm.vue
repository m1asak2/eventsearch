<template>
  <div class="wrapper">
    <form action="">
      <div class="form-group">
        <label for="keyword">キーワード</label>
        <input required type="text" placeholder="AND検索" style="width :100%" />
      </div>
      <div class="form-group">
        <label class="d-block">開催日</label>
        <div class="form-check-inline" style="width:100%">
          <input
            type="date"
            name="start_from"
            id="id_start_from"
            class="form-control"
            value="2021-04-06"
            style="width :100%"
          />
          〜
          <input
            type="date"
            name="start_to"
            id="id_start_to"
            class="form-control"
            value="2021-10-06"
            style="width :100%"
          />
        </div>
      </div>
      <div class="form-check-inline" style="width:100%">
        <div class="form-group" style="width:50%">
          <label for="">開催地</label>
          <input type="text" style="width:95%" />
        </div>
        <div class="form-group" style="width:50%">
          <label for="limit">取得イベント数</label>
          <select id="limit" name="limit" class="form-control">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </select>
        </div>
      </div>
      <button type="submit" class="btn btn-primary" style=" width:100%">
        検索
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    items: {
      type: Array,
      default: () => [
        { label: 'テキスト', key: 'text1', type: 'text' },
        { label: 'テキスト2', key: 'text2', type: 'date' }
      ]
    },
    reset: {
      type: Boolean,
      default: false
    },
    result: {
      type: Boolean,
      default: false
    },
    oKbuttonName: {
      type: String,
      default: 'OK'
    },
    resetButtonName: {
      type: String,
      default: 'Reset'
    },
    labelWidth: {
      type: String,
      default: '4'
    },
    formWidth: {
      type: String,
      default: '8'
    },
    isPush: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      form: {},
      show: false
    }
  },
  methods: {
    onSubmit(evt: Event) {
      evt.preventDefault()
      this.$emit('decide', this.form)
      // console.log('show form')
      // console.log(this.form)
    },
    onReset(evt: Event) {
      evt.preventDefault()
      // Reset our form values

      // 早い
      // for (const key in this.form) {
      //   this.form[key] = ''
      // }
      // 安全？
      // for (const k of Object.keys(this.form)) {
      //   this.form[k] = {}
      // }
      this.form = {}
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
  width: 100%;
}
.wrapper {
  /* width: 80%; */
  grid-template-rows: 50px 200px;
  grid-template-columns: 1fr 2fr;
}
</style>
