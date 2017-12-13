import lazyloading from '@/utils/lazyLoading'

export default [{
  text: '주식',
  path: '/stock',
  icon: 'show_chart',
  pri: 200,
  component: lazyloading('stock', true)
}]
