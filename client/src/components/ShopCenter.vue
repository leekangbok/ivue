<template>
  <iu-toolbar-nav searchBox>
    <template slot="title">
      <v-icon large>home</v-icon>
      <!-- <span class="hidden-xs-only">Dshop</span> -->
    </template>
    <!-- <v-avatar size="90px"
          slot="title">
          <img slot="title" src="src/assets/shopping_search_logo.jpg">
      </v-avatar> -->
    <div class="d-flex align-center"
      style="margin-left: auto">
      <Notifications></Notifications>
      <MyShop></MyShop>
    </div>
  </iu-toolbar-nav>
</template>

<script>
import Notifications from './Notifications'
import MyShop from './MyShop'

export default {
  data() {
    return {
      search: ''
    }
  },
  components: {
    Notifications,
    MyShop
  }
}
</script>
