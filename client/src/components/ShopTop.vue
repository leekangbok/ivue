<template>
  <iu-toolbar-nav title="로고"
    height="30px">
    <div class="d-flex align-center"
      style="margin-left: auto">
      <v-btn small
        outline>로그인
      </v-btn>
      <MoreApps></MoreApps>
    </div>
  </iu-toolbar-nav>
</template>

<script>
import MoreApps from './MoreApps'
import Notifications from './Notifications'
import Accounts from './Accounts'

export default {
  components: {
    MoreApps,
    Notifications,
    Accounts
  }
}
</script>
