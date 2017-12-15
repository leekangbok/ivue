import axios from 'axios'

export default {
  get(url, { request = {}, callback = () => {}, errback = () => {} } = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(url, request)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  post(url, { request = {}, callback = () => {}, errback = () => {} } = {}) {
    return new Promise((resolve, reject) => {
      axios
        .post(url, request)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  put(url, { request = {}, callback = () => {}, errback = () => {} } = {}) {
    return new Promise((resolve, reject) => {
      axios
        .put(url, request)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  delete(url, { request = {}, callback = () => {}, errback = () => {} } = {}) {
    return new Promise((resolve, reject) => {
      axios
        .delete(url, request)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  }
}
