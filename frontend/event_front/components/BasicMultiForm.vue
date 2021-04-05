<template>
  <b-container style="min-height: 10vh; width:100%">
    <b-form style="width:70%">
      <b-row v-for="(item, index) in items" :key="index" class="my-1">
        <b-col :sm="labelWidth" style="text-align: right">
          <label :for="item.key">{{ item.label }}</label>
        </b-col>
        <b-col :sm="formWidth">
          <b-row v-if="item.type === 'radio'">
            <b-col v-for="choice in item.choices" :key="choice.key">
              <input
                v-model="form[item.key]"
                type="radio"
                :value="choice.key"
              />{{ choice.label }}
            </b-col>
          </b-row>
          <b-row v-else>
            <b-form-input
              :id="item.key"
              v-model="form[item.key]"
              :type="item.type"
              :max="item.max"
              :min="item.min"
            />
          </b-row>
        </b-col>
      </b-row>
      <b-button v-if="true" type="button" variant @click="onReset">{{
        resetButtonName
      }}</b-button>
      <b-button
        type="button"
        :disabled="isPush"
        variant="primary"
        @click="onSubmit"
        >{{ oKbuttonName }}</b-button
      >
    </b-form>
    <template v-if="result">
      <b-button type="button" variant="dark" @click="show = !show"
        >Show result</b-button
      >
      <b-card v-if="show" class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </template>
  </b-container>
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
