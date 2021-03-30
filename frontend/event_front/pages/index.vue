<template>
  <div>
    <div>
      <Logo />
      <basic-multi-form :items="fields" @decide="sendData"> </basic-multi-form>
      <!-- <h1 class="title">
        event_front
      </h1> -->
    </div>
    <div>
      <card :items="event_data"></card>
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
import Vue from 'vue'
import BasicMultiForm from '@/components/BasicMultiForm.vue'
import card from '@/components/eventTable.vue'
interface GetForm {
  keyword: string
  address: string
  count: number
  start_from: string
  start_to: string
}
interface SendForm {
  keyword: string[]
  address: string[]
  count: number
  start_from: string
  start_to: string
}
export type DataType = {
  connpassApi: string
  fields: {
    label: string
    key: string
    type: string
    min?: number
    max?: number
  }[]
  data: []
  event_data: {
    day: string
    time: string
    title: string
    img: string
    group: string
    link: string
    address: string
  }[]
}
export default Vue.extend({
  components: { BasicMultiForm, card },

  data(): DataType {
    return {
      connpassApi: '/api/connpass',
      fields: [
        { label: 'キーワード', key: 'keyword', type: 'text' },
        { label: '開催地', key: 'address', type: 'text' },
        { label: 'From', key: 'start_from', type: 'date' },
        { label: 'To', key: 'start_to', type: 'date' },
        { label: '取得イベント数', key: 'count', type: 'number', min: 0 }
        // { label: '並び順', key: 'aiu', type: 'number', min: 0, max: 1 }
      ],
      data: [],
      event_data: [
        {
          day: '2020/10/02',
          time: '20:00',
          title:
            '【iCARE Dev Meetup #18】技術顧問が語る、Ruby on Rails実践開発',
          address: '〒150-0001 東京都渋谷区神宮前６丁目３５−3',
          img:
            'https://connpass-tokyo.s3.amazonaws.com/thumbs/40/d8/40d8ac364f946e9ce377eb74baf74f7d.png',
          group: 'aiueo',
          link: 'https://icare.connpass.com/event/201662/'
        },
        {
          day: '2020/10/02',
          time: '12:00',
          title:
            '登壇枠増！！【初心者歓迎】「○○（APIなど）を使ってみた」LT大会!!',
          address: '秋葉原駅から徒歩5分（申込確定後詳細ご連絡）',
          img:
            'https://connpass-tokyo.s3.amazonaws.com/thumbs/fd/6a/fd6a08b00d1b4b281cbfd03f037fe2e3.png',
          group: 'kkddda',
          link: 'https://icare.connpass.com/event/201662/'
        }
      ]
    }
  },
  methods: {
    async sendData(data: GetForm) {
      let SendData: SendForm = {
        keyword: data.keyword.split(' '),
        address: data.address.split(' '),
        start_from: data.start_from,
        start_to: data.start_to,
        count: data.count
      }
      console.log('data')
      console.log(data)
      console.log('SendData')
      console.log(SendData)
      // var self = this
      console.log('ev')
      const response = await this.$axios
        // .$post(this.connpassApi, data)
        .$post(this.connpassApi, SendData)
        .catch(error => {
          return error.response
        })
      this.event_data = response
    }
  }
})
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
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
