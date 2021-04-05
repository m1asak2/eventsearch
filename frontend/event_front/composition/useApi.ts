import { reactive, toRefs } from '@vue/composition-api'
import { NuxtAxiosInstance } from '@nuxtjs/axios'
interface SendForm {
  keyword: string[]
  address: string[]
  count: number
  // eslint-disable-next-line camelcase
  start_from: string
  // eslint-disable-next-line camelcase
  start_to: string
}
interface eventData {
  day: string
  time: string
  title: string
  address: string
  img: string
  group: string
  link: string
}
type baseState = {
  response: eventData[]
  otherError: Error | null
  isLoading: boolean
}
interface GetForm {
  keyword: string
  address: string
  count: number
  // eslint-disable-next-line camelcase
  start_from: string
  // eslint-disable-next-line camelcase
  start_to: string
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
export default ($axios: NuxtAxiosInstance, url: string) => {
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
  const postData = async (data: GetForm) => {
    const convertedData: SendForm = {
      keyword: data.keyword.split(' '),
      address: data.address.split(' '),
      start_from: data.start_from,
      start_to: data.start_to,
      count: data.count
    }
    const res = await $axios.post(url, convertedData).catch(error => {
      return error.res
    })
    state.response = res.data
  }
  return { ...toRefs(state), postData }
}
