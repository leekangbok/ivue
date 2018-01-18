import lazyloading from '@/utils/lazyLoading'

export default [{
    text: 'People',
    path: '/customer',
    icon: 'people_outline',
    pri: 201,
    component: lazyloading('customer', true)
  },
  {
    path: '/customer/add',
    component: lazyloading('customer/CustomerAdd')
  }
]
