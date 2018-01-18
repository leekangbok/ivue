import lazyloading from '@/utils/lazyLoading'

// const bitcoin = {
//   text: '축구',
//   path: '/blog/bitcoin',
//   icon: 'attach_money',
//   component: lazyloading('blog/bitcoin')
// }

// const python = {
//   text: '농구',
//   path: '/blog/python',
//   icon: 'attach_money',
//   component: lazyloading('blog/python')
// }

const dentalShop = {
  text: '치과#',
  path: '/edent/main',
  component: lazyloading('edent/main')
}

export default [{
  text: '프로젝트',
  icon: 'toc',
  pri: 100,
  model: true,
  children: [dentalShop]
}]
