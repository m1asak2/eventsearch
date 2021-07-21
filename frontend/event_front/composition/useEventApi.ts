import useApi from '@/composition/useApi'
import { toRefs, reactive } from '@nuxtjs/composition-api'
// import { NuxtAxiosInstance } from '@nuxtjs/axios'
import { EventData, DisplayForm, SendForms } from '@/types/interfaces'
import { DisplayToSendForm } from '~/composition/ConvertForm'

type baseState = {
  response: EventData[]
  error: Error | null
  isLoading: boolean
}

export default () => {
  const apiState = reactive<baseState>({
    response: [],
    error: null,
    isLoading: false
  })
  const apiPostTrigger = async (data: DisplayForm) => {
    const convertedData: SendForms = DisplayToSendForm(data)
    const { response, otherError, isLoading, postData } = useApi('/api')
    apiState.isLoading = isLoading as any
    await postData(convertedData)
    apiState.response = response as any
    apiState.error = otherError as any
  }
  return {
    ...toRefs(apiState),
    apiPostTrigger
  }
}
