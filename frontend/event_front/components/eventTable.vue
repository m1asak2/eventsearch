<template>
  <div>
    <template v-if="items.length > 0">
      <h4 class="eventHeader">イベントHit : {{ items.length }}件</h4>
    </template>
    <template v-else>
      <h4 class="eventHeader">
        イベントは見つかりませんでした
      </h4>
    </template>
    <table>
      <thead>
        <!-- <tr>
          <th v-for="field in header" :key="field">{{ field }}</th>
        </tr> -->
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item">
          <td>
            {{ item.day }}
            <p class="time">{{ item.time }}</p>
          </td>
          <td><img :src="item.img" alt="Image" /></td>
          <td class="title">
            <a :href="item.link" target="_blank">{{ item.title }}</a>
          </td>
          <td>{{ item.address }}</td>
          <td>{{ item.group }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from '@nuxtjs/composition-api'
import { EventData } from '@/types/interfaces'
export default defineComponent({
  props: {
    header: {
      type: Array,
      default: () => ['date', 'cover', 'title', 'address', 'group']
    },
    items: {
      type: Array as PropType<EventData[]>,
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
.eventHeader {
  background-color: rgb(231, 229, 229);
  width: 100%;
  margin: 0 5px 5px 5px;
}
.time {
  font-size: 40px;
}
.title {
  font-size: 18px;
}
tr {
  border-bottom: 1px solid #ced4da;
  border-radius: 0.25rem;
}
</style>
