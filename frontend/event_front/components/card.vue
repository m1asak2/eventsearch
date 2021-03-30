<template>
  <div>
    <b-row v-for="item in items" :key="item" class="border-top">
      <b-col md="2" class="text-center">
        <h1>{{ item.day }}</h1>
      </b-col>
      <b-col md="1">
        <b-card-img
          :src="item.img"
          alt="Image"
          class="rounded-0"
          style="max-width: 5rem;"
        ></b-card-img>
      </b-col>
      <!-- <b-col>
            <b-card-body :title="item.day">
          </b-col> -->
      <b-col md="5">
        <h3>
          <a :href="item.link" target="_blank" rel="noopener noreferrer"></a
          >{{ item.title }}
        </h3>
      </b-col>
      <b-col md="">
        <p>{{ item.address }}</p>
      </b-col>
      <b-col md="">
        <p>{{ 'グループ:' + item.group }}</p>
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    items: {
      type: Array,
      default: () => [
        {
          day: '2020/10/02',
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
          title:
            '登壇枠増！！【初心者歓迎】「○○（APIなど）を使ってみた」LT大会!!',
          address: '秋葉原駅から徒歩5分（申込確定後詳細ご連絡）',
          img: 'https://picsum.photos/900/250/?image=3',
          group: 'kkddda',
          link: 'https://icare.connpass.com/event/201662/'
        }
      ]
    }
  }
})
</script>
