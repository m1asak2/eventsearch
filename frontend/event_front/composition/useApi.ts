import { reactive, toRefs } from '@vue/composition-api'
import { EventData, SendForms } from '@/types/interfaces'
import axios from 'axios'
type baseState = {
  response: EventData[]
  otherError: Error | null
  isLoading: boolean
}
// 各型は参考まで
type Options = {
  headers: {
    'X-transaction-ID'?: string
    'x-api-key'?: string
    Authorization: string
    'Content-Type'?: string
  }
}
export default (url: string) => {
  const state = reactive<baseState>({
    response: [
      {
        day: '2020/10/02',
        time: '20:00',
        title: '【iCARE Dev Meetup #18】技術顧問が語る、Ruby on Rails実践開発',
        address: '〒150-0001 東京都渋谷区神宮前６丁目３５−3',
        img:
          'https://connpass-tokyo.s3.amazonaws.com/thumbs/40/d8/40d8ac364f946e9ce377eb74baf74f7d.png',
        group: 'aiueo',
        link: 'https://icare.connpass.com/event/201662/'
      }
    ],
    otherError: null,
    isLoading: false
  })
  const postData = async (data: SendForms) => {
    const res = await axios.post(url, data).catch(error => {
      return error.res
    })
    state.response = res.data
  }
  return { ...toRefs(state), postData }
}
