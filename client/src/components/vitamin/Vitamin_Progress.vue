<template>
<div>
    <div class="row" v-for="vitamin in vitamin_summary" :key="vitamin.id">
      <template v-if="vitamin.goal && vitamin.amount">
          <div class="col-sm-4">
            <b-button pill size='s' style="font-size: 0.8em;"
            variant="outline-info" class="w-100" @click="onSubmitQuick(vitamin)">
              {{vitamin.name}}</b-button>
          </div>
          <div class="col-sm-8 pt-1">
            <b-progress height="1.5rem" :max="vitamin.goal">
              <b-progress-bar :value="vitamin.amount">
                <span><strong>{{ vitamin.amount}} / {{ vitamin.goal }}
                </strong></span>
              </b-progress-bar>
            </b-progress>
          </div>
        </template>
        <template v-else-if="vitamin.goal">
          <div class="col-sm-4">
            <b-button pill size='s' style="font-size: 0.8em;"
            variant="outline-info" class="w-100" @click="onSubmitQuick(vitamin)">
              {{vitamin.name}}</b-button>
          </div>
          <div class="col-sm-8 pt-1">
            <b-progress height="1.5rem" :max="vitamin.goal">
              <b-progress-bar :value=0>
                <span><strong>0 / {{ vitamin.goal }}
                </strong></span>
              </b-progress-bar>
            </b-progress>
          </div>

        </template>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import Tools from '@/components/mixins/Tools';

export default {
  name: 'VitaminProgress',
  mixins: [Tools],
  computed: {
    vitamin_summary() {
      return this.$store.state.vitamin_summary;
    },
  },
  data() {
    return {
      addWaterForm: {
        date: '',
        size: '',
      },
    };
  },
  methods: {
    onSubmitQuick(vit) {
      const payload = {
        date: this.getCurrentDate(),
        qty: 1,
      };
      this.addVitaminRecord(vit.vitamin_id, payload);
    },
    addVitaminRecord(vid, payload) {
      const path = `http://rasp-srv:8000/vitamins/record/?vit_id=${vid}`;
      axios.post(path, payload)
        .then(() => {
          this.$emit('clicked', true);
          this.$store.dispatch('getCurrentVitamins');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  mounted() {
    // vitamin section
    this.$store.dispatch('getCurrentVitamins');
  },
};
</script>
