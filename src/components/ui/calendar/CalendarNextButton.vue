<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { reactiveOmit } from "@vueuse/core";
import { ChevronRight } from "lucide-vue-next";
import { CalendarNext, type CalendarNextProps, useForwardProps } from "reka-ui";
import { cn } from "~/lib/utils";
import { buttonVariants } from "~/components/ui/button";

const props = defineProps<
  CalendarNextProps & { class?: HTMLAttributes["class"] }
>();

const delegatedProps = reactiveOmit(props, "class");

const forwardedProps = useForwardProps(delegatedProps);
</script>

<template>
  <CalendarNext
    :class="
      cn(
        buttonVariants({ variant: 'outline' }),
        'h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100',
        props.class,
      )
    "
    v-bind="forwardedProps"
  >
    <slot>
      <ChevronRight class="h-4 w-4" />
    </slot>
  </CalendarNext>
</template>
