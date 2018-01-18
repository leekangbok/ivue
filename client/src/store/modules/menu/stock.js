import lazyloading from '@/utils/lazyLoading'

export default [{
  text: '주식',
  path: '/stock',
  pri: 200,
  component: lazyloading('stock', true)
}]
