<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <template>
            <th v-for="field in header" :key="field" class="th">{{ field }}</th>
          </template>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item">
          <td>
            {{ item.day }}
            <p style="font-size: 50px">{{ item.time }}</p>
          </td>
          <td><img class="img" :src="item.img" alt="Image" /></td>
          <td>
            <a :href="item.link" target="_blank" class="link">{{ item.title }}</a></td>
          </td>
          <td>{{ item.address }}</td>
          <td>{{ item.group }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
interface GetForm {
  keyword: string
  address: string
  count: number
  start_from: string
  start_to: string
}
export default Vue.extend({
  props: {
    header: {
      type: Array,
      default: () => ['date', 'cover', 'title', 'address', 'group']
    },
    items: {
      type: Array,
      default: () => [
        {
          day: '2020/10/02',
          time: '12:00',
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
  }
})
</script>
<style scoped>
.th {
  font-size: 15px;
  /* background-color: rgb(218, 214, 214); */
}
.td {
  font-size: 20px;
}
.table {
  margin: 10px auto;
  padding: 10px auto;
}
.img{
  width: 8rem;
  
}
.link{
  color: black;
  border-bottom: 1px solid black;
}
</style>
