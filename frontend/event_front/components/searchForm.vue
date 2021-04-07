<template>
  <div class="container">
    <form action="" class="row">
      <div class="col-sm-8 offset-sm-2">
        <div class="form-group">
          <label for="keyword">キーワード</label>
          <input
            required
            type="text"
            placeholder="AND検索"
            style="width :100%"
          />
        </div>
        <div class="form-group">
          <label class="d-block">開催日</label>
          <div class="form-check-inline">
            <input
              type="date"
              name="start_from"
              id="id_start_from"
              class="form-control"
              value="2021-04-06"
            />
            〜
            <input
              type="date"
              name="start_to"
              id="id_start_to"
              class="form-control"
              value="2021-10-06"
            />
          </div>
        </div>
        <div class="form-group">開催地</div>
        <div class="form-group">
          <label for="limit">取得イベント数</label>
          <select name="limit" id="limit" class="form-control">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </select>
        </div>
      </div>
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
.form-group > label {
  font-weight: bold;
}
</style>
